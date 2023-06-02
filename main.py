import game
import innocent
import murderer
import sheriff
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





  # на примере MurdererActions написать функцию для невиновного



  # нужно чтобы в список l бесконечно вводили игроков пока не напишут какое-то стоп-слово


def Game():
  game.StartGame()
  game.EnterPlayers()
  game.ShowPlayers()
  game.PlayerRole()
  if role == 1:
    innocent.InnocentActions()
  elif role == 2:
    BotMurdererActions()
    sheriff.SheriffActions()
  elif role == 3:
    murderer.MurdererActions()


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
