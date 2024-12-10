import asyncio
import requests
from bs4 import BeautifulSoup
from telegram import Bot

TELEGRAM_BOT_TOKEN = '7479855899:AAHy40QiC8kY-GjWA7doBHYkIyBAV12vrD0'
TELEGRAM_CHANNEL_ID = '@BigHeads_Coin'
URL = 'https://time.ir'

async def scrape_and_send():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract content
        span_content = soup.find('span', class_='quoteText').get_text(strip=True)
        author_content = soup.find('a', class_='quoteAuthor').get_text(strip=True)
        
        # Format message
        message = f"{span_content}\n\n{author_content}\n\n@Bigheads_coin"

        # Send message to Telegram
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        await bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message[:4096])
        print("Message sent to Telegram channel successfully!")
    except Exception as e:
        print(f"Error: {e}")

async def main():
    while True:
        await scrape_and_send()
        await asyncio.sleep(5 * 60 * 60)

if __name__ == '__main__':
    asyncio.run(main())