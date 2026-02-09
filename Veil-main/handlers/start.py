from telegram import Update
from telegram.ext import ContextTypes
from utils.keyboards import join_keyboard
from utils.texts import phase_text
from core.game import Game


games = {}


async def start_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
chat_id = update.effective_chat.id
if chat_id in games:
await update.message.reply_text("❌ Game already running")
return
games[chat_id] = Game(chat_id)
await update.message.reply_text(
phase_text("Joining") + "\nClick to join",
reply_markup=join_keyboard()
)
