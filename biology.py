
import random
from random import randint

class unit:
    def __init__(self, role, group, x, y):
        self.x = x
        self.y = y
        self.role = role
        self.pos = [[x,y]]
        self.Energy = 80
        self.ID = group
        self.Group = group
        self.Connection = 0.1 * randint(0,10)
        self.topo = {}
        self.times = 0 #record how many times this unit has catch food 


    def unitMove(self):
        return randint(1,4)
	
    def save_catch_shape(self,node_obj):
    	group =  [x for x in node_obj.values() if x.Group == self.Group]
    	if len(group) > 1:
    		dist_mat = {}; direct_mat = {}
    		for node in group:
    			others = [x for x in group if x !=node]
    			dist_mat[node.ID] = []; direct_mat[node.ID] = []
    			for other in others:
    				dist_mat[node.ID] += [dist_2pt(node.x,node.y,other.x,other.y)]
    				direct_mat[node.ID] += [direct_2pt(node.x,node.y,other.x,other.y)]
    		self.times += 1 
    		self.topo[self.times] = [dist_mat,direct_mat]


class organic():
    def __int__(self,group,dist_mat={},direct_mat={}):
        self.group = group
        dist_mat = dist_mat
        direct_mat = direct_mat
    #all info can be transform to ATCG format, 
    def generate_geneCode():
        a = 1

#def geneCode(num):
#    out = bin(num)
#for i in range(100): print i,int(bin(i).replace('0b',''),2)

