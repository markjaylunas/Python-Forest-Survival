import sys
from os import system
import time
import msvcrt
import random

class Entity:
    def __init__(self,name,hp,attack):
        self._name = name
        self._hp = hp
        self._attack = attack

    def fights(self,object,action=None):
        damage = 0
        if action != None:
            if action == 'evade':
                x=random.choice([2,3,4])
                if 0 == random.choice([0,1]):
                    typer('\tYou dodged enemy attack.\n')
                    typer('\tReceived damage 0.')
                    self._hp+=x
                    typer('\n\tRecovered HP {}'.format(x))
                    sleeper(5)
                    system('cls')
                    
                else:
                    typer('\tNot fast enough!\n')
                    damage =object._attack+x
                    self._hp-=damage
                    typer('\tHp -{}.\n'.format(damage))
                    sleeper(5)
                    system('cls')
                    
            else:
                if action == 'punch':
                    damage = self._attack+random.choice([0,1,2])
                elif action == 'kick':
                    damage = self._attack+random.choice([1,2])
                
                object._hp -= damage
                typer('\tYour {} dealt a damage of {}.'.format(action,damage))
                typer('\n\t{}\'s HP -{}\n'.format(object._name,damage))
                print('\n\t{}\'s turn...'.format(object._name))
                sleeper(3.5)
                system('cls')
        else:
            damage = 0
            damage = self._attack+random.choice([0,1])
            object._hp -= damage
            des1='\n\t{} hits you hard.'.format(self._name)
            des2='\n\tWhile thinking of a strategy {} caught you offguard.'.format(self._name)
            des3='\n\t{} attacks and you can\'t defend.'.format(self._name)
            typer(random.choice([des1,des2,des3]))
            typer('\n\t{}\'s HP -{}\n'.format(object._name,damage))
            
            sleeper(4)
            system('cls')
    def check_hp(self):
        if self._hp > 0:
            return True
        else:
            return False

class Player(Entity):
    def __init__(self,name,hp,attack):
        Entity.__init__(self,name,hp,attack)

    def get_name(self):
        question1 = "\n\tWhat's your name?\n"
        typer(question1)
        player_name = input("\t>")
        self._name = player_name
        

    def statusH(self):
        hpbar=''
        max_hp = 30
        if self._hp > max_hp:
            left = self._hp - max_hp
            for i in range(left):
                hpbar+=u'\u2593'
            for i in range(max_hp-left):
                hpbar+=u'\u2592'
        else:
            for i in range(self._hp):
                hpbar+=u'\u2592'

        print('\n\t'+symbs[0]+symbs[1]*38+symbs[0])
        print(  '\t'+symbs[3]+'__ '+self._name+' __________________________________'[:-len(self._name)]+symbs[4])
        print('\t'+symbs[3]+' '*38+symbs[4])
        print('\t'+symbs[3]+' HP: {}                                 '.format(hpbar)[:-len(hpbar)]+symbs[4])
        print('\t'+symbs[3]+' '*38+symbs[4])

class Enemy(Entity):
    def __init__(self,name,hp,attack,loot=None):
        Entity.__init__(self,name,hp,attack)
        if loot is None:
            self._loot = []
        else:
            self._loot = loot
    def statusE(self):
        hpbar=''
        for i in range(self._hp):
            hpbar+=u'\u2592'
        print(  '\t'+symbs[3]+'__ '+self._name+' __________________________________'[:-len(self._name)]+symbs[4])
        print('\t'+symbs[3]+' '*38+symbs[4])
        print('\t'+symbs[3]+' HP: {}                                 '.format(hpbar)[:-len(hpbar)]+symbs[4])
        print('\t'+symbs[3]+' '*38+symbs[4])
        print('\t'+symbs[0]+symbs[2]*38+symbs[0])
    def defeated(self):
        typer('\n\t'+'{} fainted.'.format(self._name))
        sleeper(1)
        typer('\n\t'+'You defeated the ')
        print('{}'.format(self._name))
        typer('\n\t'+'walking...')
        sleeper(3)
        system('cls')


def menu():
    system('cls')
    print('\n\t'+symbs[0]+symbs[1]*31+symbs[0])
    print('\t'+symbs[3]+' '*31+symbs[4])
    print('   ╔═╗┌─┐┬─┐┌─┐┌─┐┌┬┐  ╔═╗┬ ┬┬─┐┬  ┬┬┬  ┬┌─┐┬  ')
    print('   ╠╣ │ │├┬┘├┤ └─┐ │   ╚═╗│ │├┬┘└┐┌┘│└┐┌┘├─┤│  ')
    print('   ╚  └─┘┴└─└─┘└─┘ ┴   ╚═╝└─┘┴└─ └┘ ┴ └┘ ┴ ┴┴─┘')
    print('\t'+symbs[3]+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'+symbs[4])
    print('\t'+symbs[3]+'          (1) - Play -         '+symbs[4])
    print('\t'+symbs[3]+'          (2) - Help -         '+symbs[4])
    print('\t'+symbs[3]+'          (3) - Quit -         '+symbs[4])
    print('\t'+symbs[3]+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'+symbs[4])
    print('\t'+symbs[3]+'  Developed by Mark Jay Lunas  '+symbs[4])
    print('\t'+symbs[0]+symbs[2]*31+symbs[0])
    option = None
    while option not in [1,2,3]:
        while True:
            try:
                option = int(input('\n\n\tEnter the option number to navigate: '))
                break
            except:
                typer('\tInvalid input.')
        
        if option == 1:
            system('cls')
            play()
        elif option == 2:
            system('cls')
            help()
        elif option == 3:
            system('cls')
            quit_game()
        else:
            typer('\tInvalid input.')

def sleeper(sec):
	time.sleep(sec)
	sys.stdout.flush()
	while msvcrt.kbhit():
        	msvcrt.getch()

def typer(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleeper(0.05)


def hero_actions():
    option = None
    print('\t'+symbs[3]+'___Action_____________________________'+symbs[4])
    print('\t'+symbs[3]+' '*38+symbs[4])
    print('\t'+symbs[3]+'(1)Punch (2)Kick (3)Evade             '+symbs[4])
    print('\t'+symbs[3]+'(0)Menu                               '+symbs[4])  
    print('\t'+symbs[0]+symbs[2]*38+symbs[0])
    while option not in [0,1,2,3]:
        while True:
            try:
                option = int(input('\n\tAction > '))
                break
            except:
                typer('\n\tInvalid input.')
        if option not in [0,1,2,3]:
            typer('\n\tInvalid input.')
    if option == 0:
        system('cls')
        menu()
    else:
        return option



def game_over():
    print('\n\t'+symbs[0]+symbs[1]*38+symbs[0])
    print('\t'+symbs[3]+'                                      '+symbs[4])
    print('\t'+symbs[3]+'    ╔═╗┌─┐┌┬┐┌─┐  ╔═╗┬  ┬┌─┐┬─┐       '+symbs[4])
    print('\t'+symbs[3]+'    ║ ╦├─┤│││├┤   ║ ║└┐┌┘├┤ ├┬┘       '+symbs[4])
    print('\t'+symbs[3]+'    ╚═╝┴ ┴┴ ┴└─┘  ╚═╝ └┘ └─┘┴└─       '+symbs[4])
    print('\t'+symbs[3]+'                                      '+symbs[4])
    print('\t'+symbs[0]+symbs[2]*38+symbs[0])
    sleeper(5)
    menu()

def won():
    print('\n\t'+symbs[0]+symbs[1]*38+symbs[0])
    print('\t'+symbs[3]+'                                      '+symbs[4])
    print('\t'+symbs[3]+'        ╦  ╦╦╔═╗╔╦╗╔═╗╦═╗╦ ╦          '+symbs[4])
    print('\t'+symbs[3]+'        ╚╗╔╝║║   ║ ║ ║╠╦╝╚╦╝          '+symbs[4])
    print('\t'+symbs[3]+'         ╚╝ ╩╚═╝ ╩ ╚═╝╩╚═ ╩           '+symbs[4])
    print('\t'+symbs[3]+'   You obtained better attributes     '+symbs[4])
    print('\t'+symbs[3]+'                                      '+symbs[4])
    print('\t'+symbs[0]+symbs[2]*38+symbs[0])
    sleeper(5)

    

def play():
    
    global add_hp
    global add_att
    hero = Player('Unkown',21+add_hp,3+add_att)
    boar = Enemy('Wild Boar',7,1)
    eagle = Enemy('Bald Eagle',8,1)
    wolf = Enemy('Gray Wolf',10,2)
    alligator = Enemy('Blind Alligator',12,3)
    bear = Enemy('Black Bear',14,4)
    lion = Enemy('Mountaion Lion',16,5)
    gorilla = Enemy('Grayback Gorilla',23,6)
    easy = [boar,eagle,wolf,alligator]
    normal =[alligator,boar,eagle,wolf,alligator,bear,lion]
    hard = [boar,lion,eagle,bear,wolf,alligator,bear,lion,gorilla]
    typer('\n\tEnter game difficulty.')
    print('\n\t(1)Easy  (2)Normal  (3)Hard')
    option = None
    while option not in [1,2,3]:
        while True:
            try:
                option = int(input('\n\t > '))
                break
            except:
                typer('\n\tInvalid input.')
        if option == 1:
            diff = easy
        elif option == 2:
            diff = normal
        elif option == 3:
            diff = hard
        else:
            typer('\n\tInvalid input.')
        
    system('cls')
    ############# INTRODUCTION  #############   
    hero.get_name()
    typer('\n\t'+'You woke up feeling dizzy and found yourself')
    typer('\n\t'+'   in the middle of unknown forest.')
    sleeper(1)
    typer('\n\t'+'The only thing you know is that you need to ')
    typer('\n\t'+'   survive and escape.')
    sleeper(1)

    for i in diff:
        typer('\n\t'+'An enemy showed up!')
        sleeper(2)
        system('cls')
        game_loop = True
        while game_loop:
            hero.statusH()
            i.statusE()
            option = hero_actions()
            if option == 1:
                hero.fights(i,'punch')
            elif option == 2:
                hero.fights(i,'kick')
            elif option == 3:
                hero.fights(i,'evade')
                
            
            if i.check_hp() == True:
                hero.statusH()
                i.statusE()
                if option !=3:
                    i.fights(hero)
                if hero.check_hp() == False:
                    system('cls')   
                    game_over()
                    menu()
                system('cls')
            else:
                if i == 'gorilla':
                    add_att+=1
                i.defeated()
                game_loop = False
    add_hp+=3
    won()
    menu()            

def help():
    print('\n\tHelp?')
    print('\n\t -To win the game, survive from the enemy attacks and until the end.')
    print('\n\t -Start the game on easy mode to win higher modes.')
    print('\n\t -The player gains additional health points for each victory.')
    print('\n\t -Discover how actions affect the enemy and implement a better strategy.')
    print('\n\t -Defeating a special enemy gives additional attack points.')
    print('\n\n\tNote:')
    print('\n\t -After you quit the game, additional attributes will reset.')
    print('\n\t -Going back to menu won\'t reset additional attributes.')
    input('\n\n\tPress ENTER to continue.')
    menu()

def quit_game():
    option = None
    while option not in ['y','n']:  
        option = input('\n\tAre you sure you want to exit?(y/n): ')
        if option.lower()  == 'y':
            typer('\n\tExiting...')
            sleeper(3)
            sys.exit()
        elif option.lower() == 'n':
            menu()
        else:
            typer('\tInvalid input.')
            system('cls')
symbs = [u'\u2588',u'\u2580',u'\u2584',u'\u258c',u'\u2590']
add_hp=0
add_att=0
menu()
