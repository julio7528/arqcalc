from __future__ import annotations

from typing import Any

from ..core.specification_resolver import extract_spec_values
from ..core.state_manager import StateManager
from ..models import ClarificationQuestion


class ClarificationManager:
    def __init__(self, workflow: dict[str, Any], state: StateManager, resolver: Any | None = None):
        self.workflow = workflow
        self.state = state
        self.resolver = resolver

    def unanswered_fields(self, stage_id: str) -> tuple[str, ...]:
        rules = self.workflow["clarification_rules"]
        answers = self.known_answers(stage_id)
        return tuple(field for field in rules["minimum_confirmed_fields"] if not answers.get(field, "").strip())

    def questions(self, stage_id: str) -> list[ClarificationQuestion]:
        rules = self.workflow["clarification_rules"]
        prompts = rules["question_prompts"]
        answers = self.known_answers(stage_id)
        fields = rules["minimum_confirmed_fields"]
        return [ClarificationQuestion(field, prompts.get(field, f"Confirme {field}."))
                for field in fields if not answers.get(field, "").strip()]

    def known_answers(self, stage_id: str) -> dict[str, str]:
        answers: dict[str, str] = {}
        if self.resolver:
            spec = self.resolver.active_specification()
            if spec:
                answers.update(extract_spec_values(spec.path.read_text(encoding="utf-8")))
        answers.update(self.state.confirmed_answers(self.workflow["workflow_id"], stage_id))
        return answers

    def record_answer(self, stage_id: str, field: str, answer: str) -> None:
        prompts = self.workflow["clarification_rules"]["question_prompts"]
        allowed = set(prompts)
        if field not in allowed:
            raise ValueError(f"Campo de esclarecimento desconhecido: {field}")
        self.state.record_answer(self.workflow["workflow_id"], stage_id, field, prompts[field], answer, confirmed=True)
