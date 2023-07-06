import game
import innocent
import murderer
import sheriff
import variables


def InitialGame():
  global roles_to_choose
  game.StartGame()
  game.EnterPlayers()
  game.ShowPlayers()
  game.PlayerRole()
  if variables.role == 2:
    variables.roles_to_choose.pop(2)
  elif variables.role == 3:
    variables.roles_to_choose.pop(3)
  game.AddRoles()
  variables.roles_to_choose = ["Innocent", "Sheriff", "Murderer"]


def Game():
  InitialGame()
  while True:

    if variables.role == 1:
      print("Your role is Innocent, you have 3 speed boosts to run from the murderer")
      innocent.InnocentActions()
      murderer.BotMurdererActions()
      sheriff.BotSheriff()
    elif variables.role == 2:
      print("Your role is Sheriff, you have to shoot the murderer")
      murderer.BotMurdererActions()
      sheriff.SheriffActions()
    elif variables.role == 3:
      print("Your role is Murderer, kill everyone in the house")
      murderer.MurdererActions()
      sheriff.BotSheriff()
    if game.WhoWon():
        return

Game()
