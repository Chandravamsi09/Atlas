import random
from typing import Dict, Optional


class CanaryPromptRouter:
    """
    Traffic splitter for Prompt A/B testing and canary version rollouts.
    Splits traffic probabilistically according to configured percentage weights.
    """
    def select_version(self, experiment_splits: Dict[str, float]) -> str:
        # Example splits: {"v1": 0.8, "v2": 0.2}
        if not experiment_splits:
            raise ValueError("No versions provided in experiment splits")

        r = random.random()
        cumulative = 0.0
        for version_id, weight in experiment_splits.items():
            cumulative += weight
            if r <= cumulative:
                return version_id
        return list(experiment_splits.keys())[0]


canary_router = CanaryPromptRouter()
