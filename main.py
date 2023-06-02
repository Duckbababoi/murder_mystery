import random

Roles = {
  'inn2': 'Bob',
  'inn1': 'Sarah',
  'sheriff': 'Emily',
  'murd': 'Jack'
}  # изненить на словарь, чтобы каждому имени соотвествовала его роль
Replics={'lost': 'You lost', 'sk':'Successful kill', 'srd': 'She was standing near Emily and Emily was the sheriff so you got shot', 'sd':'You killed the sheriff, now it` s going to be much safer, but Sarah is near, she can get the gun', 'aj':'You have already killed Jack, kill other players.', 'ab':'You have already killed Bob, kill other players.',  }
# сделать словарь из фраз которые будут показываться
# сделать комментарии с объясниями что делает каждая функция
phrases = {"test": "test"}
role = 0
IsSmbDead = False


def StartGame():#вступление игры
  intro = 'welcome to murder mystery'
  print(f"{intro:^65}")
  input('press any key to start')


def AddRole():
  global Roles
  for i, j in Roles.items():
    if isinstance(j, (int, float)):
      Roles[i] = GenerateRole()


def GenerateRole(choose: list):
  pass


def PlayerRole(): #случайная роль игрока
  global role
  choose = random.randint(1, 3)
  if choose == 1:
    print('You are innocent, survive the mass murder')
    role = 1
  if choose == 2:
    print('You are sheriff, find and shoot the murderer')
    role = 2
    Roles = {
      'Innocent': 'Bob',
      'Innocent2': 'Sarah',
      'Murderer': 'Emily',
      'Innocent3': 'Jack'
    }
  if choose == 3:
    print('You are murderer, kill all the people. Who is your first victim?')
    Roles = {
      'Innocent': 'Bob',
      'Innocent2': 'Sarah',
      'Sheriff': 'Emily',
      'Innocent3': 'Jack'
    }
    role = 3
  ShowPlayers()


def KillPlayer(index):#убирает из списка игрока которого убили
  Roles.pop(index)


def ShowPlayers():#показывает список игроков
  for i, j in Roles:
    print(j)


def KillProcess(index):#прецесс убийства где и убирается из списка мертвый персонаж и выводится список игроков
  KillPlayer(index)
  print('People left:')
  ShowPlayers()


def IsKillSuccessful(): #проверка если убийство было удачным
  if random.randint(0, 100) % 2 == 0:
    return True
  else:
    return False


def IsPlayerInList(name):#проверка если есть такой игрок в списке
  for i in Roles:
    if name.capitalize() == i:
      return True
  return False


def MurdererActions():# тут все дейтвия убийцы
  name = input("Type name of your victim:")
  if IsPlayerInList():
    if IsKillSuccessful():
      KillProcess(Roles.index(name))
      ShowPlayers()
    else:
      print(name, " was with ", random.choice(Roles))
  else:
    pass
    # попросить пользователя ввести имя еще раз до момента пока он не введет его правильно


def BotMurdererActions():#действия убийцы, только убийца бот а у игрока другая роль
  global IsSmbDead
  chance = random.randind(0, 1)
  if chance:
    death = random.choice(Roles)
    Roles.pop(death)
    IsSmbDead = True
  else:
    IsSmbDead = False


# на примере BotMurdererActions написать функцию для шерифа-бота


def SheriffActions(): #действия игрока в роли шерифа
  name_sher = input(
    'You think you know who is a musderer? Then shoot him. Type a name')
  # после вопроса шерифа знает ли он кто убийца сделать какие-то действия
  question = input('Do you want to team up with someone? Yes or no?')
  if question.capitalize == 'Yes':
    question2 = input('Who would u like to team up with?')
    ShowPlayers()

  def TeamUp():
    if IsPlayerInList(question2):
      if IsSmbDead != False:
        print("Your team up with", question2)
      else:
        print("Your can not team up because somebody is dead")


def InnocentActions():#действияя игрока в роли невинного
  pass
  # на примере MurdererActions написать функцию для невиновного


def EnterPlayers():
  stop=input('type stop to stop getting list of names')
  while stop!='stop':
    for i in Roles:
      print (i)
  # нужно чтобы в список l бесконечно вводили игроков пока не напишут какое-то стоп-слово


def Game():
  StartGame()
  EnterPlayers()
  ShowPlayers()
  PlayerRole()
  if role == 1:
    InnocentActions()
  elif role == 2:
    BotMurdererActions()
    SheriffActions()
  elif role == 3:
    MurdererActions()


Game()
"""
def MurdererActions() :
  def Replics():
    GotShot='She was standing near Emily and Emily was the sheriff so you got shot'
    Lost='You lost'
    kill='Successfull kill'
    SarahNear='You killed the sheriff, now it` s going to be much safer, but Sarah is near, she can get the gun'
    DeadEmily='While you were trying to kill already dead Emily, Sarah took the pistol and shot you.'
    DeadBob='You have already killed Bob, kill other players.'
    DadJack='You have already killed Jack, kill other players.'
    victim2='So who is your second victim?'
    eliminated='You know what? You are eliminated'
    replics=['She was standing near Emily and Emily was the sheriff so you got shot']
  print('Write the name')
  name=input()
  if name == l[1]:
    Replics(replics[0])
    print('You lost')
    quit()
  if name == l[0]:
    print('Successful kill')
    KillProcess(0)
  if name == l[2]:
    print('You killed the sheriff, now it` s going to be much safer, but Sarah is near, she can get the gun')
    KillProcess(2)
    PlayerList()
  if name == l[3]:
    print('Successful kill')
    KillProcess(3)
    PlayerList()
  print('Who is the second victim?(write the name)')
  name2=input()
  if name==l[3] and name2==l[1]:
    print('She was standing near Emily and Emily was the sheriff so you got shot')
    print('You lost')
    quit()
  if name==l[0] and name2==l[1]:
    print('She was standing near Emily and Emily was the sheriff so you got shot')
    print('You lost')
    quit()
  if name==l[2] and name2==l[2]:
    print('While you were trying to kill already dead Emily, Sarah took the pistol and shot you.')
    print('You lost.')
    quit()
  if name==l[0] and name2==l[3]:
    print('Successful kill')
    KillProcess(3)
    PlayerList()
  if name==l[3] and name==l[0]:
    print('Successful kill')
    KillProcess(0)
    PlayerList()
  if name==l[0] and name2==l[0]:
    print('You have already killed Bob, kill other players.')
    l.pop(0)
    print('people left')
  for i in l:
    print(i)
  print('So who is your second victim?')
  if name==l[3] and name2==l[3]:
    print('You have already killed Jack, kill other players.')
    l.pop(3)
    print('people left')
    for i in l:
      print(i)
  print('So who is your second victim?')
  again=input()
  if  name==l[3] and name2==l[2]:
    print('You killed the sheriff, it must be much safer for now, but Sarah is near, she can get the gun.')
    l.pop(3, 2)
    print('people left')
    for i in l:
      print(i)
  if name==l[0] and name2==l[2]:
    print('You killed the sheriff, it must be much safer for now, but Sarah is near, she can get the gun.')
    l.pop(0, 2)
    print('people left')
    for i in l:
      print(i)
  if name==[2] and name2==[1]:
    print('Successful kill')
    l.pop(1, 2)
    print('people left')
    for i in l:
      print(i)
  again=input()
  if name==[3] and name2==[3] and again==[3]:
    print('You know what? You are eliminated')
    print('you lost')
    quit()
  if name==[0] and name2==[0] and again==[0]:
    print('You know what? You are eliminated')
    print('you lost')
    quit()
  if again==l[2]:
    print('You killed the sheriff, it must be much safer for now.')
    print('People left:')
    print('Sarah')
    print('Jack')
  if again==l[1]:
    print('She was standing near Emily and Emily was the sheriff so you got shot')
    print('You lost')
    quit()
  if name==l[0] and name2==l[0] and again==l[3]:
    print('Successful kill')
    l.pop(0, 3)
    print('people left')
    for i in l:
      print(i)
  if name==l[3] and name2==l[3] and again==l[0]:
    print('Successful kill')
    l.pop(0, 3)
    print('people left')
    for i in l:
      print(i)
  print('Who is your third victim? Write a name')
  name3=input() 
MurdererActions()

  """
