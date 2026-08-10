# will be used to generate random numbers
import random

#This define function is used so that the game will loop once a round is over
def play():

 #This is used to create a header
  
 print('========================================')
 print('Rock | Paper | Scissors | Lizard | Spock ')
 print ('========================================')
 
# This empty print is used to create space between the game header and the game explanation
print()

# This is so the players know which number correlates to which symbol - game instructions
 print ('1) ✊ - rock')
 print ('2) ✋ - paper')
 print ('3) ✌️ - scissors')
 print ('4) 🦎 - lizard')
 print ('5) 🖖 - spock')

#For spacing to improve readability
 print()

#players are prompted to chose 'rock' 'paper' 'scissors' 'lizard' or 'spock using numbers
 player = int(input ('Pick a number (1-5):  '))

#This is used so the correct symbol is picked and printed out
 if player == 1:
   print ('You chose:✊ ')
 elif player == 2:
  print ('You chose:✋ ')
 elif player == 3: 
  print ('You chose:✌️')
 elif player == 4:
  print ('You chose:🦎 ')
 elif player == 5: 
  print ('You chose: 🖖' )
 else:
  print ('Wrong input')

#Random is being used to generate random numbers but this code means only 1,2,3,4 or 5 will be picked

computer = random.randint(1,5)

# This is to give the randomly generated number a symbol so they player knows what the computer 'picked'
 if computer == 1:
  print ('CPU chose:✊ ')
 elif computer == 2:
  print ('CPU chose:✋ ')
 elif computer == 3: 
  print ('CPU chose:✌️')
 elif computer == 4:
  print ('CPU chose:🦎 ')
 elif computer == 5: 
  print ('CPU chose: 🖖' )
 else:
  print ('Error')

# Player chooses rock
 if player == 1 and computer == 1:
   print ('You tied')
 elif player == 1 and computer == 2:
   print ('You lost')
 elif player == 1 and computer == 3:
   print ('You won')
 elif player == 1 and computer == 4:
   print ('You won')
 elif player == 1 and computer == 5:
   print ('You lost')

#Player chooses paper
 if player == 2 and computer == 1:
  print ('You won')
 elif player == 2 and computer == 2:
   print ('You tied')
 elif player == 2 and computer == 3:
   print ('You lost')
 elif player == 2 and computer == 4:
   print ('You lost')
 elif player == 2 and computer == 5:
   print ('You won')

#Player chooses scissors
 if player == 3 and computer == 1:
   print ('You lost')
 elif player == 3 and computer == 2:
   print ('You won')
 elif player == 3 and computer == 3:
   print ('You tied')
 elif player == 3 and computer == 4:
   print ('You won')
 elif player == 3 and computer == 5:
   print ('You lost')
