from typing import Dict


class ROUGEMetric:
    """Recall-Oriented Understudy for Gisting Evaluation (ROUGE-1, ROUGE-L)."""

    def calculate(self, candidate: str, reference: str) -> Dict[str, float]:
        cand_tokens = set(candidate.lower().split())
        ref_tokens = set(reference.lower().split())

        if not ref_tokens or not cand_tokens:
            return {"rouge1_f1": 0.0, "rouge1_precision": 0.0, "rouge1_recall": 0.0}

        overlap = len(cand_tokens & ref_tokens)
        precision = overlap / len(cand_tokens)
        recall = overlap / len(ref_tokens)
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

        return {
            "rouge1_f1": round(f1, 4),
            "rouge1_precision": round(precision, 4),
            "rouge1_recall": round(recall, 4)
        }


rouge_metric = ROUGEMetric()
