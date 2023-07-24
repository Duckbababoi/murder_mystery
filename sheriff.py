import variables
import game
import random
import murderer


def SheriffActions():  #действия игрока в роли шерифа
  shoot = 'Do you already want to shoot someone? Yes or no?'
  shoot = input(f"{shoot:^65}")
  if shoot.capitalize() == 'Yes':
    game.ShowPlayers()
    name_sher = input(
      'You think you know who is a murderer? Then shoot him. Type a name')
    while not game.IsPlayerInList(name_sher):
      game.ShowPlayers()
      name_sher = 'You wrote invalid name, please try again'
      name_sher=input(f"{name_sher:^65}")
    if game.IsPlayerInList(name_sher) and variables.Roles[
        name_sher.capitalize()] == variables.roles_to_choose[2]:
      win = 'she was murderer, good job. You win!'
      print(f"{win:^65}")
      game.Sheriff_win()
    elif game.IsPlayerInList(name_sher) and variables.Roles[
        name_sher.capitalize()] != variables.roles_to_choose[2]:
      shot_inn = 'You shot an innocent, be more careful next time'
      print(f"{shot_inn:^65}")
      print(variables.Replics['lost'])
      quit

  if shoot.capitalize() == 'No':
    question = 'Do you want to team up with anyone? Yes or no?'
    question = input(f"{question:^65}")

    if question.capitalize() == 'Yes':
      game.ShowPlayers()
      question2 = input('Who would u like to team up with?')
      if game.IsPlayerInList(question2.capitalize()):
        if variables.IsSmbDead != False:
          print("Your team up with", question2.capitalize())
        else:
          smb_dead = "Your can not team up because somebody is dead"
          print(f"{smb_dead:^65}")


def BotSheriff():
  instant_shot = random.randint(1, 2)

  bot_team = random.randint(1, 2)

  bot_teamup = random.randint(1, len(variables.Roles))

  if instant_shot == 1:
    variables.instant_person = random.choice(list(variables.Roles.keys()))
    variables.instant_person_role = variables.Roles[instant_person]
    variables.Roles.pop(instant_person)

    if instant_person_role == variables.roles_to_choose[2]:
      game.Sheriff_win()

      print('You win!')
    if variables.role == 3 and instant_person == "Me":
      sh_you = 'Sheriff shot you'
      print(f"{sh_you:^65}")
      print(variables.Replics['lost'])
    if variables.role == 1 and instant_person == "Me":
      sh_you_m = 'Sheriff shot you, but he made a mistake'
      print(f"{sh_you_m:^65}")
      print(game.Replics['lost'])
  if instant_shot == 2:
    team_up = random.choice(list(variables.Roles.keys()))
    if team_up == 'Me':
      sh_team = 'Sheriff wants to team up with you, do you want to team up with her? Yes or no? If you are murderer and you will team up with sheriff, you will instantly kill her.'
      input(f"{sh_team:^65}")
      if variables.role == 1 and sh_team.capitalize() == 'Yes':
        rules = 'You teamed up with sheriff. Now if murderer kills you, sheriff will shoot him, if murderer kills sheriff you can pick up the gun and shoot the murderer, sheriff can`t shoot you'
        print(f"{rules:^65}")
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
          print('Sheriff hasn\'t team up with anybody')

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