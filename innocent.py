import variables
import random
import sheriff
import murderer
import game

def InnocentActions():  #действияя игрока в роли невинного
  boost=3
  desision=input('You went to the bathroom and then you hear a scream, would you like to check what happened (Type Check), hide in the bathroom (Type Hide), or run in another room(type Run)?')
  if desision.capitalize()=='Check':
    killed=random.randint(1,6)
    victim=random.randint(1,4)
    
    if killed==1:
      print('Looks like someone from the guests decided to kill everyone')
      if victim==1:
        gun=input('You walk around and you find a dead sheriff would you like to pick up a gun? Yes or no?')
        if gun.capitalize()=='Yes':
          pass
        if gun.capitalize()=='No':
          pass
      else:
        pass
    else: 
      print('Murderer caught you and killed you, you lost')
      
      
      
    
  