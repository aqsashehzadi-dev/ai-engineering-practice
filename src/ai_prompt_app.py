import logging
from pathlib import Path

from src.prompt_validator import validate_prompt
from src.config_manager import load_config
from src.results_manager import save_result


logger = logging.getLogger(__name__)


def process_prompt(prompt, config_path, results_path):
    """Validate a prompt and save a demo processing result."""

    cleaned_prompt = validate_prompt(prompt)
    config = load_config(config_path)

    model = config["model"]

    # Demo response only — no real AI API call
    response = f"Demo response from {model}: {cleaned_prompt}"

    save_result(
        prompt=cleaned_prompt,
        response=response,
        status="success",
        filename=results_path,
    )

    logger.info("Prompt processed successfully.")

    return response


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    config_file = Path("data") / "ai_config.json"
    results_file = Path("data") / "prompt_results.csv"

    try:
        result = process_prompt(
            "Explain AI Engineering",
            config_file,
            results_file,
        )
        print(result)

    except Exception:
        logger.exception("Prompt processing failed.")