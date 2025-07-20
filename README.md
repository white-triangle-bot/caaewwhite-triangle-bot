# White Triangle Bot for Bybit P2P

Этот бот мониторит P2P-объявления на Bybit и уведомляет тебя в Telegram, когда находится возможность «белого треугольника».

## Настройка

1. Замени в `main.py` значения:
   - `BOT_TOKEN` на твой токен от @BotFather
   - `CHAT_ID` на твой Telegram ID

2. Установи зависимости:
   ```
   pip install -r requirements.txt
   ```

3. Запусти бота:
   ```
   python main.py
   ```

## Развёртывание на Render.com

1. Зарегистрируйся на https://render.com и подключи свой GitHub.
2. Создай Web Service, выбери этот репозиторий.
3. В поле **Start command** укажи:
   ```
   python main.py
   ```
4. Выбери **Free plan** и запусти.

Готово! Бот будет работать 24/7 и присылать уведомления в Telegram.
