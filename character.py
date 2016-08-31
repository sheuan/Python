import random

from combat import Combat

class Character(Combat):
    experience=0
    attack_limit=10
    base_hit_points=10
    
    def attack(self):
        roll=random.randint(1, self.attack_limit)
        
        if self.weapon=='sword':
            roll+=1
        elif self.weapon=='axe':
            roll+=2
        
        return roll>4
    
    def get_weapon(self):
        weapon_choice=input("Weapon ([S]word, [A]xe, [B]ow): ").lower()
        
        if weapon_choice in 'sab':
            if weapon_choice=='s':
                return 'sword'
            if weapon_choice=='a':
                return 'axe'
            if weapon_choice=='b':
                return 'bow'
        else:
            return self.get_weapon()  #Don't just call function get_weapon, always call an instance of it
        
    def __init__(self, **kwargs):
        self.name=input("Name: ")
        self.weapon=self.get_weapon()
        self.hit_points=self.base_hit_points
        
        for key,value in kwargs.items(): #if user wants to add any other attribute to character
            setattr(self,key,value)
        
