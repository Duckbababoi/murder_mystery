import variables
import game
import random

def SheriffActions():  #действия игрока в роли шерифа
  shoot ='Do you already want to shoot someone? Yes or no?'
  input(f"{shoot:^65}")
  if shoot.capitalize() == 'Yes':
    name_sher = input(
      'You think you know who is a musderer? Then shoot him. Type a name')
  game.ShowPlayers()
  while not game.IsPlayerInList(name_sher):
    name_sher = 'You wrote invalid name, please try again'
    input(f"{name_sher:^65}")
    game.ShowPlayers()
  if game.IsPlayerInList(
        name_sher) and name_sher.capitalize() == variables.Roles['murd']:
          win='she was murderer, good job. You win!'
          print(f"{win:^65}")
          game.Sheriff_win()
  elif game.IsPlayerInList(
      name_sher) and name_sher.capitalize() != variables.Roles['murd']:
    shot_inn='You shot an innocent, be more careful next time'
    print(f"{shot_inn:^65}")
    print(variables.Replics['lost'])
  
  if shoot.capitalize == 'No':
    question = 'Do you want to team up with anyone? Yes or no?'
    input(f"{question:^65}")
  
  if question.capitalize == 'Yes':
    question2 = input('Who would u like to team up with?')
    game.ShowPlayers()

  def TeamUp():
    if game.IsPlayerInList(question2):
      if variables.IsSmbDead != False:
        print("Your team up with", question2)
      else:
        smb_dead="Your can not team up because somebody is dead"
        print(f"{smb_dead:^65}")

def BotSheriff():
  instant_shot=random.randint(1,2)
  
  bot_team=random.randint(1,2)

  bot_teamup=random.randint(1, len(variables.Roles))

  if instant_shot==1:
    instant_person = random.choice(list(variables.Roles.keys()))
    instant_person_role = variables.Roles[instant_person]
    variables.Roles.pop(instant_person)
  
    if instant_person_role == variables.roles_to_choose[2]:
      game.Sheriff_win()

      print('You win!')
    if variables.role == 3 and instant_person == "Me":
      sh_you='Sheriff shot you'
      print(f"{sh_you:^65}")
      print(variables.Replics['lost'])
    if variables.role == 1 and instant_person == "Me":
      sh_you_m='Sheriff shot you, but he made a mistake'
      print(f"{sh_you_m:^65}")
      print(game.Replics['lost'])
  if instant_shot==2:
    if bot_team==1:
        sh_team='Sheriff wants to team up with you, do you want to team up with her?'
        print(f"{sh_team:^65}")
    elif bot_team==2:
      team_up=random.choice(list(variables.Roles.keys('Bob', 'Sarah', 'Emily', 'Jack')))
      