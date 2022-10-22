import numpy as np
import random
from random import randint
import time
from utils import get_target_position, can_move 
from player_A_method import player_A
from player_B_method import player_B


class Board():
    def __init__(self, row, col):
        self.mat = np.zeros((row, col))  
        self.mat[:11, 26]= 8
        self.mat[10, :11]= 9
        self.mat[10, :]= 9
        
        self.mat[10, 11:13]= 0
        self.mat[10, 35:37]= 0
        
        self.mat[4, 2:20] = 1
        self.mat[4, 32:50] = 3
        self.generate_food()
    
        self.node_obj1 ={}
        self.node_obj3 ={}

        self.player_A_count = 0
        self.player_B_count = 0
        
        self.player_a = player_A(self.mat)
        self.player_b = player_B(self.mat)

    def generate_food(self):
        node_dict = get_target_position(self.mat, 1)

        while True:
            x = randint(25, self.mat.shape[0]-1)
            y = randint(0, self.mat.shape[1]-1)
            if [x,y] not in node_dict.values():
                self.mat[x][y] = 2
            if len(get_target_position(self.mat, 2)) > 4: 
                break

    def update(self):
        self.mat = self.player_a.catch(self.mat)
        self.mat = self.player_b.catch(self.mat)

        self.food_move()
        self.output()
        time.sleep(0.2)


    def output(self):
        node_dict = get_target_position(self.mat,2)
        left = "number of food left: " + str(len(node_dict)) + '\n'
        left += "player A: %d,  player B: %d \n" % (self.player_a.food_count,  self.player_b.food_count) 
        sep = f'\n------------------********--------------------\n' 
        out = ""

        for row in self.mat: 
            #s1 = [str(x).replace('0', color('.')) for x in row]
            s1 = [str(int(x)).replace('0', ' ') for x in row]
            s2 = [x.replace('8', '|') for x in s1]
            s2 = [x.replace('9', '_') for x in s2]
            out += ' '.join(s2) + '\n'
        print(format(out + left + sep))

    def food_move(self):
        node_dict = get_target_position(self.mat, 2)
        if len(node_dict) < 2: 
            self.generate_food()
            node_dict = get_target_position(self.mat,2)

        direct = random.randint(1,4)
        select = node_dict[random.randint(1,len(node_dict))]
        x, y = select

        ret = can_move(x, y, direct, self.mat)
        if ret: 
            x2, y2 = ret
            self.mat[x][y] = 0
            self.mat[x2][y2] = 2

