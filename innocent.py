import variables
import random
import sheriff
import murderer
import game

boost=3
def InnocentActions():  #действияя игрока в роли невинного
  global boost
  desision=input('You went to the bathroom and then you hear a scream, would you like to check what happened (Type Check), hide in the bathroom (Type Hide), or run in another room(type Run)?')
  if desision.capitalize()=='Check':
    killed=random.randint(1,6)
    victim=random.randint(1,4)
    
    if killed==1:
      print('Looks like someone from the guests decided to kill everyone')
      if victim==1:
        gun=input('You walk around and you find a dead sheriff would you like to pick up a gun? Yes or no?')
        if gun.capitalize()=='Yes':
          print('Now you can shoot a muderer when ')
        if gun.capitalize()=='No':
          pass
      else:
        print('You found a dead innocent, you need to investigate who is the murderer')
    else: 
      boost_question1=input('Murderer saw you, would you like to use your speed boost? Yes or No? If you won`t use it, murderer will kill you ')
      if boost_question1.capitalize()=='Yes':
        boost-=1
        question=input('You ran away from the murderer, now you have one boost less but the most important is that you are still alive. Would you like to hide somewhere (Type Hide) or go to other rooms to find other guests (Type Search)?')
        if question.capitalize()=='Hide':
          pass
        if question.capitalize()=='Search':
          pass
        
      if boost_question1.capitalize()=='No':
        print('Murderer caught you and killed you, you lost')
        
      
      
    
  