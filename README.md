# Target Pokémon Bot

This bot checks Target for Pokémon TCG product restocks and sends Telegram alerts when items are found in stock.

## Setup

1. Add your `TELEGRAM_TOKEN` and `TELEGRAM_CHAT_ID` to Railway's environment variables.
2. Deploy the bot as a worker service.
3. Logs will show status; Telegram alerts notify when product is in stock.

## Dependencies

- Python 3.9+
- Playwright
- Requests

## Deployment

Use Railway or run locally with:

```bash
pip install -r requirements.txt
python main.py
```
