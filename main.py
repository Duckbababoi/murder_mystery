import game
import innocent
import murderer
import sheriff
import variables

def InitialGame():
  game.StartGame()
  game.EnterPlayers()
  game.ShowPlayers()
  game.PlayerRole()
  if variables.role == 2:
    variables.roles_to_choose.pop(2)
  elif variables.role == 3:
    variables.roles_to_choose.pop(3)
  game.AddRoles()

def Game():
  InitialGame()
  while True:
    if variables.role == 1:
      innocent.InnocentActions()
    elif variables.role == 2:
      murderer.BotMurdererActions()
      sheriff.SheriffActions()
    elif variables.role == 3:
      murderer.MurdererActions()
Game()
