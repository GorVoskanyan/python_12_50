class Warrior:
    def __init__(self, nickname):
        self.nickname = nickname
        self.health = 100
        
    def is_alive(self):
        return self.health
    
    def attack(self, enemy):
        enemy.health -= 20
        

def fight(warrior1, warrior2):
    while warrior1.is_alive() and warrior2.is_alive():
        attacker, enemy = __import__('random').sample([warrior1, warrior2], k=2)
        print(f"{enemy.nickname} has been attacked from {attacker.nickname}")
        attacker.attack(enemy)
        print(warrior1.health, '|', warrior2.health)
        __import__('time').sleep(3)
        
    print(f"Win {warrior1.nickname if warrior1.is_alive() else warrior2.nickname}")
        
        
def main():
    warrior1 = Warrior('Subzero')
    warrior2 = Warrior('Scorpion')
    fight(warrior1, warrior2)
    

if __name__ == '__main__':
    main()