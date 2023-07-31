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
  stop = input('Type stop to stop adding new player or just a name:')
  while stop != 'stop':
    variables.Roles[stop] = 0
    stop = input('Type stop to stop adding new player or just a name:')


def WhoWon():
  if variables.roles_to_choose[2] in variables.Roles.values():
    if  len(variables.Roles)<=2:
      print('Murderer won')
      return True
    return False
  else:
    print('Sheriff and innocents won!')
    return True

def IsSheriffAlive():
  for i in variables.Roles:
    if variables.roles_to_choose[1] in i:
      return True
      
    else:
      return False

def SherBotForInn():
  variables.instant_person = random.choice(list(variables.Roles.keys()))
  variables.instant_person_role = variables.Roles[instant_person]
  variables.Roles.pop(instant_person)

  if instant_person_role == variables.roles_to_choose[2]:
      game.Sheriff_win()
  if variables.role == 1 and instant_person == "Me":
      sh_you_m = 'Sheriff shot you, but he made a mistake'
      print(f"{sh_you_m:^65}")
      print(game.Replics['lost'])
    if instant_person_role == variables.roles_to_choose[2]:
      game.Sheriff_win()

      print('You win!')

  if instant_shot == 2:
    team_up = random.choice(list(variables.Roles.keys()))
    if team_up == 'Me':
      sh_team = 'Sheriff wants to team up with you, do you want to team up with her? Yes or no? If you are murderer and you will team up with sheriff, you will instantly kill her.'
      input(f"{sh_team:^65}")

  if variables.role == 1 and sh_team.capitalize() == 'Yes':
        rules = 'You teamed up with sheriff. Now if murderer kills you, sheriff will shoot him, if murderer kills sheriff you can pick up the gun and shoot the murderer, sheriff can`t shoot you'
        print(f"{rules:^65}")
  else:
    if variables.Roles[team_up] == variables.roles_to_choose[0]:
      global sheriff_team_up
      if random.randint(0, 1) == 1 and not variables.IsSmbDead:
        variables.sheriff_team_up = team_up
        print('Sheriff has team up with somebody')
      else:
        variables.sheriff_team_up = 0
        print('Sheriff hasn`t teamed up with anybody')
    elif variables.Roles[team_up] == variables.roles_to_choose[2]:
      for i, j in variables.Roles:
        if j == variables.roles_to_choose[1]:
          global IsSmbDead
          global death
          variables.death = i
          variables.IsSmbDead = True
          game.KillPlayer(i)
      dead_sheriff = 'You can`t find the sheriff anywhere, maybe something happened to him...'
        print(f"{dead_sheriff:^65}")
        check = input(
          'Do you want to find out what happened to the sheriff? Yes or no?')
        if check.capitalize() == 'Yes':
          WhereisSheriff=random.choice(list(variables.Rooms.keys()))
          what_room=input('What room would you like to check? Office, kitchen, bedroom, living room or garden? Type the name oof the room')
          while what_room.capitalize()!=WhereisSheriff:
           what_room=input('You didnt find  sheriff in this room, type anothor room you want to check')
           
          found_gun=input('You found the sheriff, he is dead, do you want to pick up the gun? Yes or No')
          if found_gun.capitalize()=='Yes':
            pick_up_gun=input('You picked up the gun, now ypu can shoot the murderer when you find out who is the murderer, or maybe you alredy know whe the murderer is? Do ypu want tp shoot someone right now/ Yes or No?')
            if pick_up_gun.capitalize()=='Yes':
              who_to_shoot=input('So who would you like to shoot?')
              game.ShowPlayers()
              if variables.roles_to_choose[2]==who_to_shoot:
                print('You shot the murderer, you won!')
                quit
              else:
                print('You shot the wrong person, you lost')
                quit
          if found_gun.capitalize()=='No' or check.capitalize() == 'No':
            hide=input('You hear someone walking nearby, what if it is a murderer? It will be better to hide, would you like to hide here, or run in another room? If you want to hide here type Hide if you want to run in another room type Run')
          if hide.capitalize()== 'Hide':
            got_found=random.randint(1,2)
            print('Murderer entered the room, now you only have to pray he wont find you')
            if got_found==1:
              print('Murderer found you and killed you, you lost. ')
              quit
            if got_found==2:
              print('Luckily murderer didn`t find you, but it`s not the end yet... ')
          if hide.capitalize()=='Run':
            die_chance=random.randint(1,3)
            print('You are going to another room, be quiet, murderer can hear you ')
            if die_chance==3:
              print('Murderer heard you and killed you, you lost')
              quit
            else:
              print('You successfully went to another room')
    

def SherBotForMurd():
  sheriff.instant_person = random.choice(list(variables.Roles.keys()))
    sheriff.instant_person_role = variables.Roles[instant_person]
    variables.Roles.pop(instant_person)
  if variables.role == 3 and instant_person == "Me":
      sh_you = 'Sheriff shot you'
      print(f"{sh_you:^65}")
      print(variables.Replics['lost'])
  if instant_shot == 2:
    team_up = random.choice(list(variables.Roles.keys()))
    if team_up == 'Me':
      sh_team = 'Sheriff wants to team up with you, do you want to team up with her? Yes or no? If you are murderer and you will team up with sheriff, you will instantly kill her.'
      input(f"{sh_team:^65}")

      if variables.roles == 3 and sh_team.capitalize() == 'Yes':
        kill_sher = 'You killed sheriff'
        print(f"{kill_sher:^65}")
    else:
      if variables.Roles[team_up] == variables.roles_to_choose[0]:
        global sheriff_team_up
        if random.randint(0, 1) == 1 and not variables.IsSmbDead:
          variables.sheriff_team_up = team_up
          print('Sheriff has team up with somebody')
        else:
          variables.sheriff_team_up = 0
          print('Sheriff hasn`t team up with anybody')
      elif variables.Roles[team_up] == variables.roles_to_choose[2]:
        for i, j in variables.Roles:
          if j == variables.roles_to_choose[1]:
            global IsSmbDead
            global death
            variables.death = i
            variables.IsSmbDead = True
            game.KillPlayer(i)

def find_key_by_value(dictionary, value_to_find):

    for key, value in dictionary.items():

        if value == value_to_find:

            return key

    return None

 

 
          