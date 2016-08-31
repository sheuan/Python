import sys
from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll
import random

class Game:
    
    def setup(self):
        self.player=Character() #This triggers name and weapon selection
        self.monsters=[
            Goblin(),
            Troll(),
            Dragon()]
        self.monster=self.get_next_monster()
        
        def get_next_monster(self):
            try:
                return self.monsters.pop(0)
            except IndexError:
                return None
            
        def monster_turn(self):
            #Check to see if monster attacks
            if self.monster.attack():
                print("The {} is attacking!".format(self.monster))#If so, tell the player
                #See if player wants to dodge
                if input('Dodge? Y/N').lower()=='y':
                    #If so, check if dodge successfull
                    #If it is, move on
                    if self.player.dodge():
                        print("You dodged successfully!")
                    #If it's not, remove 1 player hit point
                    else:
                        print("Failed to dodge!")
                        self.player.hit_points-=1
                else:
                    print("{} hit you for 1 point".format(self.monster))
                    self.player.hit_points-=1
            else: #If the monster doesn't attack, inform player
                print("{} isn't attacking this turn".format(self.monster))
            
            
        def player_turn(self):
            #Let the player attack,rest or quit
            player_choice=input("[A]ttack, [R]est, [Q]uit").lower()
            #If player attacks:
            if player_choice=='a':
                print("You're attacking {}".format(self.monster))
                #Check if successful
                if self.player.attack():
                    #If so, check if monster dodges
                    if self.monster.dodge():
                        #If dodged, print that
                        print("You're attack failed!")
                    #If not, subtract the appropriate amount of hit points form the monster
                    else:
                        if self.player.leveled_up():
                            self.monster.hit_points-=2
                        else:
                            self.monster.hit_points-=1
                        print("You hit{} with your {}".format(
                        self.monster, self.player.weapon))
                else:
                    print("You missed your attack!")
            #if not a good attack, tell player
            
            #If player wants to rest:
            elif player_choice=='r':
                #Call player.rest() method
                self.player.rest()
            #If player wants to quit, exit game
            elif player_choice=='q':
                sys.exit()
            #If they pick anything else, re-run this method
            else:
                self.player_turn()
            
        def cleanup(self):
            #If monster has no more hit points:
            if self.monster.hit_points<=0:
                #Increase player's experience
                self.player.experience+=self.monster.experience
                #Print according message
                print("You killed {}".format(self.monster))
                self.monster=self.get_next_monster()
                
        def __init__(self): #The actual game loop
            self.setup()
            
            while self.player.hit_points and (self.monster or self.monsters):
                print('\n'+'='*20)
                print(self.player)
                self.monster_turn()
                print('-'*20)
                self.player_turn()
                self.cleanup()
                print('\n'+'='*20)
                
            if self.player.hit_points:
                print('Congratulations! You win.')
            elif self.monsters or self.monster:
                print('You lost!')
            sys.exit()
            
Game()
            
            
            