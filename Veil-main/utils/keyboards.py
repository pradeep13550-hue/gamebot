from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def join_keyboard():
return InlineKeyboardMarkup([
[InlineKeyboardButton("➕ Join Game", callback_data="join")]
])


def vote_keyboard(players):
return InlineKeyboardMarkup([
[InlineKeyboardButton(p.username, callback_data=f"vote_{p.id}")]
for p in players
])
