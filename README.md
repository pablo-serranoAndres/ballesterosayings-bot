# 🤖 ballesterosayingsbot

A Telegram bot to manage sayings from a book by Aragonese authors. Supports CRUD operations, multilingual filtering, and role-based access control (RBAC).

## 🚀 Features

### User actions

- Add a saying
- Change language
- Filter sayings by field
- Edit a saying
- View sayings

### Admin actions

- Manage users (approve/deny access)
- Delete sayings

## 🛠️ Tecnologías

- Python 3.10+
- pyTelegramBotAPI (`telebot`)

## ⚙️ Installation

Follow these steps to install and run the bot locally:

1. **Clone the repository**

```bash
git clone https://github.com/pablo-serranoAndres/ballesterosayings-bot.git
cd ballesterosayings-bot
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Create a Telegram bot on [BotFather](https://t.me/BotFather)**

```bash
Go to BotFather on Telegram.
Create a new bot and obtain the bot token.
```

4. **Configure the bot**

```bash
Open main.py.

Replace 'BOT_TOKEN' with your Telegram bot token.
```

5. **Run the bot**

```bash
python main.py
```

6. **Optional: Virtual Environment (recommended)**

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
