from telegram import Update
from telegram.ext import ContextTypes
from handlers.start import games
from utils.keyboards import vote_keyboard


async def start_vote(update: Update, context: ContextTypes.DEFAULT_TYPE):
game = games.get(update.effective_chat.id)
if not game:
return


game.phase = "vote"
players = [p for uid, p in game.players.items() if uid in game.alive]
await update.message.reply_text(
"🗳 Voting Phase",
reply_markup=vote_keyboard(players)
)
