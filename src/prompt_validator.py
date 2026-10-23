class InvalidPromptError(ValueError):
    """Raised when an AI prompt is invalid."""
    pass


def validate_prompt(prompt):
    if not isinstance(prompt, str):
        raise TypeError("Prompt must be a string.")

    cleaned_prompt = prompt.strip()

    if not cleaned_prompt:
        raise InvalidPromptError(
            "Prompt cannot be empty."
        )

    return cleaned_prompt