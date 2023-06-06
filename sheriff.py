import variables
import game


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
