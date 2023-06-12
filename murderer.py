import random
import variables
import game


def MurdererActions():  # тут все дейтвия убийцы
  name = "Type name of your victim:"
  input(f"{name:^65}")
  if game.IsPlayerInList():
    if game.IsKillSuccessful():
      game.KillProcess(variables.Roles.index(name))
      game.ShowPlayers()
    else:
      print(name, " was with ", random.choice(variables.Roles))
  else:
    pass


def BotMurdererActions(
):  #действия убийцы, только убийца бот а у игрока другая роль
  global IsSmbDead
  chance = random.randint(0, 1)
  if chance:
    death = random.choice(list(variables.Roles.keys()))
    variables.Roles.pop(death)
    IsSmbDead = True
  else:
    IsSmbDead = False
