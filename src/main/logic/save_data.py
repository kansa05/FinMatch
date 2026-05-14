import json
from datetime import datetime, timezone
from pathlib import Path


def save_training_example(cleaned_profile, pathway, recommendations):
    """
    Append one rule-based training example to data/training_data.jsonl.
    """
    project_root = Path(__file__).resolve().parents[3]
    data_dir = project_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    output_path = data_dir / "training_data.jsonl"

    training_example = {
        "cleaned_profile": cleaned_profile,
        "pathway": pathway,
        "recommended_investments": recommendations,
        "label_source": "rule_based",
        "feedback": None,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    with output_path.open("a", encoding="utf-8") as file:
        json.dump(training_example, file)
        file.write("\n")
