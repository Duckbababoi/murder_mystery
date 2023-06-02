def BotMurdererActions():#действия убийцы, только убийца бот а у игрока другая роль
  global IsSmbDead
  chance = random.randind(0, 1)
  if chance:
    death = random.choice(Roles)
    Roles.pop(death)
    IsSmbDead = True
  else:
    IsSmbDead = False