from telegram import Update
from telegram.ext import ContextTypes
from handlers.start import games


async def night_phase(update: Update, context: ContextTypes.DEFAULT_TYPE):
game = games.get(update.effective_chat.id)
if not game:
return


game.assign_roles()
game.phase = "night"


for uid, user in game.players.items():
await context.bot.send_message(
uid,
f"🌙 Night Phase\nYour role: {user.role}"
)
