# Automatic McDonald's Code Claimer

<p align="center">
  <img alt="Archived" src="https://img.shields.io/badge/status-archived-lightgrey" />
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" />
  <img alt="Selenium" src="https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=fff" />
</p>

> [!CAUTION]
> This is an unfinished historical experiment. It relies on obsolete Discord and McDonald's page structures, injects a Discord token into browser storage, and should not be used with a real account.

The script was intended to request a code from a specific Discord message interaction and then step through a McDonald's feedback form with Selenium.

## Current state

The project is not production-ready:

- Discord server, channel, and action-message IDs must be supplied manually.
- Login depends on direct token injection.
- Discord and survey selectors are hard-coded.
- Receipt values are hard-coded into the generated survey URL.
- Several answers are selected randomly.
- The feedback loop still pauses for manual confirmation.
- Final reward-code retrieval was never completed.
- The included `chromedriver.exe` may not match an installed Chrome version.

## Code flow

1. Load identifiers and a Discord token from `.env`.
2. Start Chrome through Selenium.
3. Inject the token and open the configured Discord channel.
4. Click a specific message component.
5. Read the first `code` element on the page.
6. Open the feedback site and construct a URL from that value.
7. Answer recognised page layouts until an unknown page is reached.

## Configuration reference

`.env.example` lists the values expected by the source:

~~~dotenv
DISCORD_TOKEN=
DISCORD_SERVER_ID=
DISCORD_CHANNEL_ID=
DISCORD_ACTION_MESSAGE_ID=
~~~

Do not populate these values unless you are working in an authorised disposable test environment. Never commit the resulting `.env` file.

## Security concerns

- A Discord token provides account access and must be treated like a password.
- Automating a normal user account can violate Discord's rules.
- Randomly completing a feedback form can submit false information.
- Hard-coded absolute XPath selectors can click the wrong control when a page changes.

For code review, inspect `main.py` without supplying credentials or allowing it to submit forms.

## Files

- `main.py`, the unfinished Selenium workflow.
- `.env.example`, required variable names with blank values.
- `chromedriver.exe`, an old bundled Chrome driver.
- `requirements.txt`, Selenium and python-dotenv versions.

## Historical setup

~~~bash
python -m pip install -r requirements.txt
~~~

The entry point is `python main.py`, but running it against live services is not recommended.

## Licence

No project-level licence is currently included.
