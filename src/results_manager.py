import csv
from pathlib import Path
import logging


class ResultsError(Exception):
    """Raised when saving results fails."""
    pass


FIELDNAMES = ["prompt", "response", "status"]
logger = logging.getLogger(__name__)

def save_result(prompt, response, status, filename):
    if not all(isinstance(value, str) for value in
               (prompt, response, status)):
        raise TypeError("All result fields must be strings.")

    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    path = Path(filename)

    try:
        file_exists = path.is_file()
        needs_header = (
            not file_exists or path.stat().st_size == 0
        )

        with path.open(
            "a", newline="", encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file, fieldnames=FIELDNAMES
            )

            if needs_header:
                writer.writeheader()

            writer.writerow({
                "prompt": prompt.strip(),
                "response": response,
                "status": status,
            })

        logger.info("Prompt result saved successfully.")

    except OSError as error:
        logger.exception("Failed to save prompt result.")
        raise ResultsError(
            "Failed to save prompt result."
        ) from error

    return path