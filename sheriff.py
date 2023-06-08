import variables
import game
import random

def SheriffActions():  #действия игрока в роли шерифа
  shoot = input('Do you already want to shoot someone? Yes or no?')
  if shoot.capitalize() == 'Yes':
    name_sher = input(
      'You think you know who is a musderer? Then shoot him. Type a name')
  game.ShowPlayers()
  while not game.IsPlayerInList(name_sher):
    name_sher = input('You wrote invalid name, please try again')
    game.ShowPlayers()
  if game.IsPlayerInList(
        name_sher) and name_sher.capitalize() == variables.Roles['murd']:
      print('she was murderer, good job. You win!')
      game.Sheriff_win()
  elif game.IsPlayerInList(
      name_sher) and name_sher.capitalize() != variables.Roles['murd']:
    print('You shot an innocent, be more careful next time')
    print(variables.Replics['lost'])
  
  if shoot.capitalize == 'No':
    question = input('Do you want to team up with anyone? Yes or no?')
  
  if question.capitalize == 'Yes':
    question2 = input('Who would u like to team up with?')
    game.ShowPlayers()

  def TeamUp():
    if game.IsPlayerInList(question2):
      if variables.IsSmbDead != False:
        print("Your team up with", question2)
      else:
        print("Your can not team up because somebody is dead")

def BotSheriff():
  instant_shot=random.randint(1,2)
  instant_person=random.randint(1, 4)
  bot_team=random.randint(1,2)
  bot_teamup=random.randint(1,4)
  if instant_shot==1:
    if instant_person==1:
      print(variables.Replics['ms']) 
      variables.Roles.pop('inn2')
    elif instant_person==2:
      print(variables.Replics['ms']) 
      variables.Roles.pop('inn1')
    elif instant_person==4:
      print('You hear a shot, the game is over, sheriif has shot the murderer')
      print('You win!')
    if game.PlayerRole()==3 and instant_person==3:
      print('Sheriff shot you')
      print(variables.Replics['lost'])
    if game.PlayerRole()==1 and instant_person==3:
      print('Sheriff shot you, but he made a mistake')
      print(game.Replics['lost'])
  if instant_shot==2:
    if bot_team==1:
      if bot_teamup==1:
        pass
      if bot_teamup==2:
        pass
      if bot_teamup==3:
        pass
      if bot_teamup==4:
        print('Sheriff wants to team up with you, do you want to team up with her?')