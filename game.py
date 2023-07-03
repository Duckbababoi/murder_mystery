import random
import variables
import sheriff
import murderer
import innocent

def StartGame():  #вступление игры
  intro = 'welcome to murder mystery'
  print(f"{intro:^65}")
  key = 'press any key to start ..'
  input(f"{key:^65}")


def PlayerRole():
  variables.role = 2


def AddRoles():
  global Roles
  for i, j in variables.Roles.items():
    if isinstance(j, (int, float)):
      variables.Roles[i] = GenerateRole()


def GenerateRole():
  global roles_to_choose
  role = random.choice(variables.roles_to_choose)
  if role != "Innocent":
    variables.roles_to_choose.pop(variables.roles_to_choose.index(role))
  return role


def KillPlayer(index):  #убирает из списка игрока которого убили
  variables.Roles.pop(index)


def ShowPlayers():  #показывает список игроков
  still_alive = 'People that still alive:'
  print(f"{still_alive:^65}")
  for j in variables.Roles:
    print(f"{j:^65}")


def KillProcess(
  index
):  #прецесс убийства где и убирается из списка мертвый персонаж и выводится список игроков
  KillPlayer(index)
  pl = 'People left:'
  print(f"{pl:^65}")
  ShowPlayers()


def IsKillSuccessful():  #проверка если убийство было удачным
  if random.randint(0, 100) % 2 == 0:
    return True
  else:
    return False


def IsPlayerInList(name):  #проверка если есть такой игрок в списке
  for i in variables.Roles:
    if name.capitalize() == i:
      return True
  return False


def EnterPlayers():
  stop = input('\n\n\n\nType stop to stop adding new player or just a name:')
  while stop != 'stop':
    variables.Roles[stop] = 0
    stop = input('Type stop to stop adding new player or just a name:')


def WhoWon():
  if variables.roles_to_choose[2] in variables.Roles:
    if  len(variables.Roles)<=2:
      print('Murderer won')
      return True
    return False
  else:
    print('Sheriff and innocents won!')
    return True
  