# Automatic McDonald's Code Claimer

> [!WARNING]
> This is an unfinished, unmaintained browser-automation experiment. It depends on old Discord and McDonald's page structures and should not be expected to work.

The script opens Chrome with Selenium, attempts to retrieve a code from a specific Discord message interaction, and walks through a McDonald's feedback form using hard-coded selectors.

## Why it is fragile

- Discord server, channel, and message identifiers are fixed through environment variables.
- Discord and survey-site HTML selectors can change at any time.
- Several form answers are selected randomly.
- The script assumes a particular code and receipt format.
- The repository contains an old `chromedriver.exe`, while modern Selenium may manage its own compatible driver.

## Requirements

```bash
python -m pip install -r requirements.txt
```

The pinned dependencies are Selenium 4.11.2 and python-dotenv 0.21.1.

## Configuration

Copy `.env.example` to `.env`:

```dotenv
DISCORD_TOKEN=
DISCORD_SERVER_ID=
DISCORD_CHANNEL_ID=
DISCORD_ACTION_MESSAGE_ID=
```

All four values are required by the script.

## Security and account safety

The implementation injects `DISCORD_TOKEN` into browser local storage. Do not use a personal/user account token: automating user accounts can violate Discord's rules and exposes full account access if the token leaks. Never commit `.env`, tokens, codes, or other account identifiers.

Only run automation against services and accounts where you have permission, and review the relevant service terms first.

## Running for code review/testing

```bash
python main.py
```

Use a disposable, authorised test environment if examining the automation. The current project is best treated as historical source code rather than a production tool.

## Current implementation

The source contains functions for Discord login, requesting a code, opening the feedback site, selecting multiple-choice/satisfaction answers, and advancing through pages. Reliable final-code retrieval was not completed.
