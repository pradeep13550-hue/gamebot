import random
from core.roles import ROLES


class Game:
def __init__(self, chat_id):
self.chat_id = chat_id
self.players = {}
self.alive = set()
self.started = False
self.phase = "join"
self.votes = {}


def add_player(self, user):
self.players[user.id] = user
self.alive.add(user.id)


def assign_roles(self):
roles = ROLES.copy()
random.shuffle(roles)
for uid, role in zip(self.players, roles):
self.players[uid].role = role


def is_alive(self, uid):
return uid in self.alive
