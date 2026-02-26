import random

class Character:
    #constructor - wil run when new object is made
    def __init__(self, name, level, health, maxDamage):
        self.name = name
        self.level = level
        self.health = levels[level-1][0]
        self.maxDamage = levels[level-1][1]
        self.damageMitigation = levels[level-1][2]
        self.XP = 0

    def inspect(self):
        print("Character name: " , self.name)
        print("Current Health: " , self.health)

    def attack(self , target):
        damage = random.randint(1,self.maxDamage)
        print(self.name , "attacks" , target.name ,  "for" , damage , "damage")
        target.takeDamage(damage)

    def takeDamage(self, attackDamage):
        mitigated = attackDamage-self.damageMitigation
        print(self.name , "takes" , mitigated , "damage")
        self.health -= mitigated
        print(self.name , "health: " , self.health)

levels = [[100, 10, 0],[110 , 15 , 1] , [120, 20, 3]]
        

hero = Character("Ennis" , 1, 100 , 20)

boss = Character("Mountain" , 2, 150 , 25)

hero.attack(boss)

boss.attack(hero)

