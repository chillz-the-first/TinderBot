# TinDog Auto-Swiper

A Selenium bot that logs into TinDog (a Tinder clone built for the *100 Days of Code* course) and likes 20 dog profiles automatically. Built for Day 50 of the course.

## What it does

1. Opens TinDog and clicks the login button.
2. Logs in through the Facebark popup (email + password in a separate browser window).
3. Dismisses the three startup popups (location, notifications, cookies).
4. Swipes right on 20 dogs, dismissing any match popups along the way.

## Tech stack

- Python 3.13
- Selenium
- python-dotenv (for credentials)
- Chrome + ChromeDriver

## Setup

Clone the repo and install the dependencies:

```bash
 pip install selenium python-dotenv
```

Create a `.env` file in the project root with your TinDog URL and Facebark credentials:

```
URL=your-personal-tindog-url
ACCOUNT_EMAIL=any-email@example.com
PASSWORD=anything
```

Facebark accepts any email and password, so the values don't need to be real.

## Run

```bash
 python main.py
```

Chrome opens, the bot logs in, dismisses the popups, and likes 20 dogs. The window stays open for 20 seconds at the end so you can watch the result, then closes.

## How it works

**Window switching.** Clicking Facebark opens the login form in a second browser window. The bot waits for two windows to exist, then switches to the one that isn't the original to fill in the form. After submitting, it switches back to the main window.

**Explicit waits.** Every interaction uses `WebDriverWait` with `expected_conditions` instead of fixed `sleep()` calls. Each step waits exactly as long as the element needs to load, so the bot doesn't fail on slow loads or waste time on fast ones.

**Match popups.** When you match with a dog, a popup covers the like button. Before each like, the bot uses `find_elements` (plural) as a non-blocking check for the popup. If one is present it dismisses it first, then likes the current dog. Each of the 20 iterations produces a like.

**Fault tolerance.** The like loop catches `TimeoutException` per card. If one card's like button never becomes clickable, the bot logs it and moves to the next card instead of crashing the whole run.

## Notes

- ChromeDriver is managed automatically by Selenium Manager (bundled with recent Selenium versions), so you don't need to download it separately.
- Facebark login runs in a popup window, not an inline iframe. If you refactor, keep the window-switching logic.

## License

MIT