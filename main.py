import requests
import time
from telegram import Bot

# === Конфигурация ===
BOT_TOKEN = '7967429095:AAFiOFRlxNTODhMqi4ngrmDl_aB5byhWgYE'  # Твой токен Telegram-бота
CHAT_ID = 430582176  # Твой Telegram ID
SPREAD_THRESHOLD = 0.80  # Минимальная прибыль (в рублях на 1 USDT)

bot = Bot(token=BOT_TOKEN)

def get_bybit_p2p_price(trade_type, asset="USDT", fiat="RUB"):
    url = "https://api2.bybit.com/fiat/otc/item/online"
    payload = {
        "userId": "",
        "tokenId": asset,
        "currencyId": fiat,
        "payment": [],
        "side": trade_type,
        "size": "",
        "page": 1,
        "amount": "",
        "authMaker": False
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    if data.get("result") and data["result"]["items"]:
        return float(data["result"]["items"][0]["price"])
    else:
        return None

def check_opportunity():
    buy_price = get_bybit_p2p_price("Buy")
    sell_price = get_bybit_p2p_price("Sell")

    if not buy_price or not sell_price:
        print("Нет данных с Bybit")
        return

    spread = sell_price - buy_price
    if spread >= SPREAD_THRESHOLD:
        message = (
            f"💰 Возможность 'белого треугольника' на Bybit!\n"
            f"🔻 Купить USDT по: {buy_price:.2f} ₽\n"
            f"🔺 Продать USDT по: {sell_price:.2f} ₽\n"
            f"📈 Профит: {spread:.2f} ₽ на 1 USDT"
        )
        bot.send_message(chat_id=CHAT_ID, text=message)
        print(message)
    else:
        print(f"Нет профита. Покупка: {buy_price:.2f}, Продажа: {sell_price:.2f}")

if __name__ == "__main__":
    while True:
        try:
            check_opportunity()
            time.sleep(15)
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            time.sleep(30)
