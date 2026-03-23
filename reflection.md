# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, it appeared to be a working number guessing game with a text input, a Submit Guess button, and a hint display. However, several bugs became clear after playing twice.

**Bug 1: Hints were backwards**
- **Expected:** When I guessed 50 and the secret number was 14, the hint should have said "Go LOWER" since 50 is greater than 14.
- **Actual:** The game said "Go HIGHER," pointing me in completely the wrong direction.

**Bug 2: Hints kept saying "Go Higher" even past the secret number**
- **Expected:** Once my guess exceeded the secret number (e.g., guessing 60 when the secret was 40), the hint should have switched to "Go LOWER."
- **Actual:** The game kept telling me to go higher all the way up to 100, only flipping direction at the very top — making the game nearly unwinnable.

**Bug 3: Score went negative**
- **Expected:** Running out of attempts should end the game with a score of 0, or at least not penalize the player below zero.
- **Actual:** The score dropped to -5 after one lost game and -10 after another, suggesting the scoring formula has a bug that subtracts points incorrectly.

**Bug 4: Game state did not reset cleanly between rounds**
- **Expected:** Starting a new game should reset the score, guess history, and secret number completely.
- **Actual:** When I opened the Developer Debug Info at the start of a new game, it still showed the guess history and score from the previous round, meaning session state was not being properly cleared.

---

## 2. How did you use AI as a teammate?

On this project I used GitHub Copilot in VS Code, including Copilot Chat and Inline Chat. One example of a correct AI suggestion was when I asked Copilot to explain the `check_guess` function in `logic_utils.py` — it correctly identified that the comparison operators were flipped, meaning `guess > secret` was returning "Go Lower" when it should return "Go Higher," and vice versa. I verified this by manually tracing through the logic with the known secret number (14) and my guess (50), confirming the condition was indeed backwards. One example of a misleading suggestion was when Copilot suggested fixing the score bug by resetting the score variable to zero at the top of the guess handler — but this would have wiped the score on every single guess, not just at the start of a new game. I caught this by reading the diff carefully and realizing the reset was in the wrong place in the code flow.

---

## 3. Debugging and testing your fixes

I decided a bug was truly fixed only when two things were true: the pytest test I wrote for it passed, and I also manually verified the behavior in the live Streamlit app. For the hint logic bug, I wrote a pytest test in `tests/test_game_logic.py` that called `check_guess(50, 14)` and asserted it returned a "lower" hint — this test failed before my fix and passed after, which confirmed the repair. I also manually played the game after the fix, starting with 50 against a secret of 14, and verified the hint correctly said "Go LOWER." Copilot helped me write the initial structure of the test and suggested the assertion format, though I had to adjust the expected return value to match what the function actually returned.

---

## 4. What did you learn about Streamlit and state?

Streamlit works differently from most programs because every time you interact with it — clicking a button, typing in a box — the entire Python script reruns from the top. I would explain it to a friend like this: imagine every button click reloads the whole page from scratch, so any variables you set earlier are gone unless you specifically save them. That's what `st.session_state` is for — it's like a small notebook Streamlit keeps between reruns so your score, your guess history, and the secret number don't disappear every time the script re-executes. This is why the game had bugs where state wasn't resetting properly between games — the session state wasn't being cleared when a new game started.

---

## 5. Looking ahead: your developer habits

One habit I want to carry forward is adding `# FIXME` comments the moment I spot something suspicious, before I even try to fix it — it kept me organized and gave Copilot a clear anchor point when I used Inline Chat. Next time I work with AI on a coding task, I would read every diff more slowly before accepting it, because the score reset bug showed me that AI can produce a change that looks right at first glance but is placed in the wrong part of the logic. This project changed how I think about AI-generated code: I used to assume that if code runs without crashing, it's probably correct, but now I understand that code can run fine and still have deeply wrong logic that only shows up when you actually play with it.
