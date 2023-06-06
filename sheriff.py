import variables
import game


def SheriffActions():  #действия игрока в роли шерифа
  shoot=input('Do you already want to shoot someone? Yes or no?')
  if shoot.capitalize()=='Yes':
    name_sher = input(
    'You think you know who is a musderer? Then shoot him. Type a name')
  game.ShowPlayers()
  if game.IsPlayerInList('Emily') and  name_sher.capitalize()==variables.Roles['murd']:
    print('she was murderer, good job. You win!')
    game.Sheriff_win()
  elif game.IsPlayerInList(name_sher) and name_sher.capitalize()!=variables.Roles['murd']:
    print('You shot an innocent, be more careful next time')
    print(variables.Replics['lost'])
  else:
    while name_sher.capitalize!=game.IsPlayerInList(variables.Roles):
      print('You wrote invalid name, please try again')
  if shoot.capitalize=='No':
    question=input('Do y')

  # после вопроса шерифа знает ли он кто убийца сделать какие-то действquestion = input('Do you want to team up with someone? Yes or no?')
  if question.capitalize == 'Yes':
    question2 = input('Who would u like to team up with?')
    game.ShowPlayers()

  def TeamUp():
    if game.IsPlayerInList(question2):
      if variables.IsSmbDead != False:
        print("Your team up with", question2)
      else:
        print("Your can not team up because somebody is dead")
