import telebot
from telebot import types

# ---------------- সেটিং শুরু ---------------- #

# ১. BotFather থেকে পাওয়া টোকেন নিচে ' ' এর ভেতর বসান
API_TOKEN = '8045074122:AAEGMj4NQ4n59exARwn_HI-7dtmpm3as_s8' 

# ২. আপনার CPAGrip থেকে কপি করা লিংক নিচে বসান
CPA_LINK = 'https://www.cpagrip.com/view.php?id=1864297'

# ৩. আপনার নিজের টেলিগ্রাম ইউজারনেম (যাতে ইউজাররা মেসেজ দিতে পারে)
ADMIN_USERNAME = '@Sahed_hossain113' 

# ---------------- সেটিং শেষ ---------------- #

bot = telebot.TeleBot(API_TOKEN)
user_data = {}

def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("💰 কাজ করুন (Task)")
    btn2 = types.KeyboardButton("👤 আমার পয়েন্ট")
    btn3 = types.KeyboardButton("💎 উইথড্র (Diamond)")
    btn4 = types.KeyboardButton("📞 সাহায্য (Help)")
    markup.add(btn1, btn2, btn3, btn4)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {'points': 0}
    
    welcome_text = (
        f"স্বাগতম {message.from_user.first_name}! 💎\n\n"
        "এটি Elite Rewards Bot এর অফিসিয়াল বট।\n"
        "এখানে টাস্ক কমপ্লিট করে ফ্রিতে ডাইমন্ড নিতে পারবেন।"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu())

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {'points': 0}

    # Task Section
    if "কাজ করুন" in message.text:
        text = (
            "✅ ডাইমন্ড পেতে নিচের লিংকে গিয়ে অ্যাপ ইন্সটল বা সার্ভে কমপ্লিট করুন:\n\n"
            f"🔗 লিংক: {CPA_LINK}\n\n"
            "⚠️ কাজ শেষ হলে পয়েন্ট অটোমেটিক জমা হবে (অথবা স্ক্রিনশট এডমিনকে দিন)।"
        )
        bot.send_message(message.chat.id, text)

    # Balance Section
    elif "আমার পয়েন্ট" in message.text:
        points = user_data[user_id]['points']
        bot.send_message(message.chat.id, f"👤 আপনার বর্তমান ব্যালেন্স: {points} Points")

    # Withdraw Section
    elif "উইথড্র" in message.text:
        points = user_data[user_id]['points']
        if points >= 1000:
            msg = bot.send_message(message.chat.id, "আপনার Free Fire UID টি লিখুন:")
            bot.register_next_step_handler(msg, process_withdraw)
        else:
            bot.send_message(message.chat.id, "❌ উইথড্র করতে মিনিমাম ১০০০ পয়েন্টস লাগবে।")

    # Help Section
    elif "সাহায্য" in message.text:
        bot.send_message(message.chat.id, f"যেকোনো সমস্যায় এডমিনকে মেসেজ দিন: {ADMIN_USERNAME}")

def process_withdraw(message):
    uid = message.text
    bot.send_message(message.chat.id, "✅ আপনার রিকোয়েস্ট জমা হয়েছে। ২৪ ঘণ্টার মধ্যে ডাইমন্ড পেয়ে যাবেন।")

print("Elite Rewards Bot is Running...")
bot.infinity_polling()
