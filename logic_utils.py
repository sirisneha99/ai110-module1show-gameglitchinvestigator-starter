import random


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.
    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."
    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).
    # FIX: Always compare as integers — removed the string conversion bug
    # that was causing hints to flip on even-numbered attempts.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📈 Go LOWER!"   # FIX: was incorrectly showing "Go HIGHER!"
    return "Too Low", "📉 Go HIGHER!"        # FIX: was incorrectly showing "Go LOWER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update score based on outcome.
    # FIX: Removed the even/odd attempt_number check that was randomly
    # adding +5 points for wrong guesses, causing scores to go negative.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5   # FIX: always subtract, never add for wrong guess

    if outcome == "Too Low":
        return current_score - 5

    return current_score