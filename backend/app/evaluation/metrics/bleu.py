import math
from typing import List, Dict, Set


class BLEUMetric:
    """BiLingual Evaluation Understudy (BLEU) n-gram precision metric."""

    def calculate(self, candidate: str, reference: str, max_n: int = 4) -> float:
        cand_tokens = candidate.lower().split()
        ref_tokens = reference.lower().split()
        if not cand_tokens or not ref_tokens:
            return 0.0

        precisions = []
        for n in range(1, max_n + 1):
            cand_ngrams = [tuple(cand_tokens[i:i+n]) for i in range(len(cand_tokens) - n + 1)]
            ref_ngrams = set(tuple(ref_tokens[i:i+n]) for i in range(len(ref_tokens) - n + 1))

            if not cand_ngrams:
                precisions.append(0.0)
                continue

            matches = sum(1 for ng in cand_ngrams if ng in ref_ngrams)
            precisions.append(matches / len(cand_ngrams))

        if any(p == 0.0 for p in precisions):
            return 0.0

        # Geometric mean
        geo_mean = math.exp(sum(math.log(p) for p in precisions) / max_n)
        
        # Brevity penalty
        bp = min(1.0, math.exp(1.0 - len(ref_tokens) / len(cand_tokens)))
        return round(bp * geo_mean, 4)


bleu_metric = BLEUMetric()
