import variables
import game
def SheriffActions(): #действия игрока в роли шерифа
  name_sher = input(
    'You think you know who is a musderer? Then shoot him. Type a name')
  # после вопроса шерифа знает ли он кто убийца сделать какие-то действия
  question = input('Do you want to team up with someone? Yes or no?')
  if question.capitalize == 'Yes':
    question2 = input('Who would u like to team up with?')
    game.ShowPlayers()

  def TeamUp():
    if game.IsPlayerInList(question2):
      if variables.IsSmbDead != False:
        print("Your team up with", question2)
      else:
        print("Your can not team up because somebody is dead")