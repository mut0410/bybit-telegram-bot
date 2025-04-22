import os

def main():
    print("Bot is starting...")
    print("Using API Key:", os.getenv("BYBIT_API_KEY"))
    print("Listening to Telegram messages...")

if __name__ == "__main__":
    main()