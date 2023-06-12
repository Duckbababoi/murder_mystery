import random
import variables


def StartGame():  #вступление игры
  intro = 'welcome to murder mystery'
  print(f"{intro:^65}")
  input('press any key to start')

def PlayerRole():
  variables.role = random.randint(1,3)

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
  print("People that still alive:")
  for j in variables.Roles:
    print(j)


def KillProcess(
  index
):  #прецесс убийства где и убирается из списка мертвый персонаж и выводится список игроков
  KillPlayer(index)
  print('People left:')
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
  stop = input('type stop to stop getting list of names')
  while stop != 'stop':
    variables.Roles[stop] = 0
    stop = input('type stop to stop getting list of names')
    
def Sheriff_win():
  win='Good job sheriff!'
  print(f"{win:^65}")
  quit
