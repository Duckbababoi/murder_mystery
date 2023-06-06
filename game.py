import random
import variables


def StartGame():  #вступление игры
  intro = 'welcome to murder mystery'
  print(f"{intro:^65}")
  input('press any key to start')


def AddRole():
  for i, j in variables.Roles.items():
    if isinstance(j, (int, float)):
      variables.Roles[i] = GenerateRole()


def GenerateRole(choose: list):
  pass


def PlayerRole():  #случайная роль игрока
  global role
  choose = random.randint(1, 3)
  if choose == 1:
    print('You are innocent, survive the mass murder')
    role = 1
  if choose == 2:
    print('You are sheriff, find and shoot the murderer')
    role = 2
    variables.Roles = {
      'inn2': 'Bob',
      'inn1': 'Sarah',
      'murd': 'Emily',
      'inn3': 'Jack'
    }
  if choose == 3:
    print('You are murderer, kill all the people. Who is your first victim?')
    variables.Roles = {
      'inn2': 'Bob',
      'inn1': 'Sarah',
      'sheriff': 'Emily',
      'inn3': 'Jack'
    }
    role = 3
  ShowPlayers()


def KillPlayer(index):  #убирает из списка игрока которого убили
  variables.Roles.pop(index)


def ShowPlayers():  #показывает список игроков
  for i, j in variables.Roles:
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
    for i in variables.Roles:
      print(i)

def Sheriff_win():
  win='Good job sheriff!'
  print(f"{win:^65}")
  quit