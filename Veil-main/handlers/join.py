from telegram import Update
from telegram.ext import ContextTypes
from handlers.start import games


async def join_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
query = update.callback_query
user = query.from_user
game = games.get(query.message.chat_id)


if not game or game.started:
await query.answer("Game already started")
return


if user.id in game.players:
await query.answer("Already joined")
return


game.add_player(user)
await query.answer("✅ Joined")
