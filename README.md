# Telegram Gifts Buyer



Automated Telegram userbot for purchasing gifts with smart prioritization, multiple recipients, and intelligent balance
management.

> 🌐 [Русская версия](README-RU.md)

## ✨ Features

- **🤖 Automated Monitoring**: Continuously scans for new gifts matching your criteria
- **🎯 Smart Prioritization**: Prioritizes rare gifts (low supply) within your price ranges
- **👥 Multi-Recipient**: Send different quantities to multiple users/channels per price range
- **💰 Balance Management**: Makes partial purchases when balance is insufficient
- **📊 Detailed Notifications**: Purchase confirmations, balance alerts, and processing summaries
- **🔧 Flexible Setup**: Simple configuration format for price ranges and recipients
- **🌍 Multi-Language**: English and Russian interface

## 🚀 Installation

```bash
git clone https://github.com/Heru934/TelegramGiftAutoBuy
cd Gifts-Buyer
pip install -r requirements.txt
```

Edit `config.ini` with your settings and run:

```bash
python main.py
```

## 🐳 Docker Usage

You can run the bot via Docker. The process includes one-time Telegram authorization and background launch.

### 1. Build the Docker image

```bash
docker compose build
```

### 2. Run the container for Telegram login (one-time setup)

```bash
docker compose run --rm gift-buyer
```

Follow the prompts to complete Telegram authorization. Your session will be saved in the `./data/` directory.

> ℹ️ This step is only required once — until your session expires or you change accounts.

### 3. Start the bot in background mode

```bash
docker compose up -d
```

The bot will start using the saved session and configuration from `config.ini`.

### 4. Stop the bot (when needed)

```bash
docker compose down
```

## ⚙️ Configuration

### Basic Settings

```ini
[Telegram]
API_ID = your_api_id                   # From https://my.telegram.org/apps
API_HASH = your_api_hash               # From https://my.telegram.org/apps
PHONE_NUMBER = +1234567890             # Your phone number
CHANNEL_ID = -100xxxxxxxxx             # Notifications channel (-100 to disable)

[Bot]
INTERVAL = 10                          # Check interval in seconds
LANGUAGE = EN                          # Interface language (EN/RU)

[Gifts]
# Format: price_range: supply_limit x quantity: recipients
GIFT_RANGES = 1-1000: 500000 x 1: @user1, 123456; 1001-5000: 100000 x 2: @channel

PURCHASE_ONLY_UPGRADABLE_GIFTS = False # Buy only upgradable gifts
PRIORITIZE_LOW_SUPPLY = True           # Prioritize rare gifts
```

### Gift Ranges Format

**Format**: multiple ranges separated by `;`  
Each range: `min_price-max_price: supply_limit x quantity: recipients`

**Examples**:

- `1-1000: 500000 x 1: @johndoe, 123456789` - Cheap gifts, 1 copy each
- `1001-5000: 100000 x 2: @channel, @user` - Mid-range, 2 copies each
- `5001-50000: 50000 x 5: 987654321` - Expensive gifts, 5 copies

**As a result**:  
`GIFT_RANGES = 1-1000: 500000 x 1: @johndoe, 123456789; 1001-5000: 100000 x 2: @channel, @user; 5001-50000: 50000 x 5: 987654321`

**Recipients can be**:

- Usernames: `@username`
- User IDs: `123456789`
- Channel names: `@channelname`

### How It Works

1. **Monitoring**: Bot checks for new gifts every `INTERVAL` seconds
2. **Filtering**: Only processes gifts matching your price ranges and supply limits
3. **Prioritization**: If `PRIORITIZE_LOW_SUPPLY = True`, processes rarest gifts first
4. **Purchasing**: Buys specified quantity for each recipient in the range
5. **Balance Check**: Makes partial purchases if balance is insufficient

## 💰 Smart Balance Management

The bot calculates how many gifts it can afford before attempting purchase:

```
Example:
- Gift costs 1500⭐, want to buy 4 copies
- Current balance: 4500⭐
- Result: Buys 3 copies, reports missing 1500⭐ for the last one
```

## 📝 Tips

- Keep balance 2-3x higher than your most expensive range
- Use multiple ranges for different strategies
- Enable notifications to monitor activity
- Test with small ranges first
- Run on VPS for 24/7 operation

---


