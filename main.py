import random
import game
import innocent
import murderer
import sheriff
import variables

# попросить пользователя ввести имя еще раз до момента пока он не введет его правильно

# на примере BotMurdererActions написать функцию для шерифа-бота

# на примере MurdererActions написать функцию для невиновного

# нужно чтобы в список l бесконечно вводили игроков пока не напишут какое-то стоп-слово


def Game():
  game.StartGame()
  game.EnterPlayers()
  game.ShowPlayers()
  game.PlayerRole()
  if variables.role == 1:
    innocent.InnocentActions()
  elif variables.role == 2:
    murderer.BotMurdererActions()
    sheriff.SheriffActions()
  elif variables.role == 3:
    murderer.MurdererActions()


Game()
