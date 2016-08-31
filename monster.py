import random

COLORS=["RED","YELLOW","BLUE","GREEN"]

class Monster:
    min_hit_points=1
    max_hit_points=1
    min_experience=1
    max_experience=1
    sound=" roar "
    weapon=" sword "
    
    def __init__(self, **kwargs):
        self.hit_points=random.randint(self.min_hit_points,self.max_hit_points)
        self.experience=random.randint(self.min_experience, max_experience)
        self.color=random.choice(COLORS)
        
        for key,value in kwargs.items():
            setattr(self,key,value)
            
    def battlecry(self):
        return self.sound.upper()
    
class Goblin(Monster): #indicates that Goblin is a subclass of Monster
    max_hit_points=3
    max_experience=2
    sound='squeak'
    
class Troll(Monster):
    min_hit_points=3
    max_hit_points=5
    min_experience=2
    max_experience=6
    sound='growl'
    
class Dragon(Monster):
    min_hit_points=5
    max_hit_points=10
    min_experience=6
    max_experience=10
    sound='raaaaaaar'
    

    
    
    



    