from utils import get_target_position, can_move, get_food, get_dist
from biology import unit
import random
from random import randint

class player_A():
    def __init__(self, mat):
        self.food_count = 0
        self.node_obj = {}
        role = 1
        node_dict = get_target_position(mat, role)
        for k,v in node_dict.items():
            self.node_obj[k] = unit(role, chr(64+k), v[0], v[1])    

    def catch(self, mat):
        for k, obj in self.node_obj.items():
            #dist_1 = get_dist(obj.x, obj.y, mat, 2)
            
            directions = list(range(1,5))
            random.shuffle(directions)

            for try_dir in directions:
                ret = can_move(obj.x, obj.y, try_dir, mat)
                if ret:
                    x2, y2 = ret
                    #dist_2 = get_dist(x2, y2, mat, 2)

                    mat[obj.x][obj.y] = 0
                    mat[x2][y2] = obj.role  

                    obj.x = x2
                    obj.y = y2

                    break

                
        mat, self.node_obj, ate = get_food(mat, self.node_obj)
        if ate:
            self.food_count += 1

        return mat 
