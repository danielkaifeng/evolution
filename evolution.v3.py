import random
from random import randint

class organic():
    def __int__(self,group,dist_mat={},direct_mat={}):
        self.group = group
        dist_mat = dist_mat
        direct_mat = direct_mat
    #all info can be transform to ATCG format, 
    def generate_geneCode():
        a = 1

def geneCode(num):
    out = bin(num)
#for i in range(100): print i,int(bin(i).replace('0b',''),2)

class unit:
    def __init__(self,group,count,x,y):
        self.x = x
        self.y = y
        self.Energy = 80
        self.ID = group + str(count)
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
    		print self.topo

class catch_unit(unit):
    def __init__(self,group,count,x,y):
        self.x = x
        self.y = y
        self.Energy = 80
        self.ID = group + str(count)

def output(mat,turn):
    node_dict = get_target_position(mat,2)
    left = "number of food left: " + str(len(node_dict)) + '\n'
    sep = '\n-------------------------------------------------------********--------------------------------------------------------------\n' 
    out = ""
    if turn == 2:
	for row in mat: 
        	out += ' '.join([str(x).replace('0','.') for x in row]) + '\n'
    	print out + left + sep
    return mat

def _int_(row,col):
    intMat = [[0 for i in range(row)] for i in range(col)]
    intMat[3][6:26]=[1]*20
    intMat = new_food(intMat)
    return intMat
def new_food(mat):
    node_dict = get_target_position(mat,1)
    while True:
	x = randint(0,len(mat[2])-1)
    	y = randint(0,len(mat[2])-1)
    	if [x,y] not in node_dict.values():
		mat[x][y] = 2
	if len(get_target_position(mat,2)) > 4: break
    return mat

def can_move(posi,direct,mat):
    x1=posi[0];y1=posi[1]
    if direct == 3: x=0;y=-1       #left 
    if direct == 4: x=0;y=1      #right
    if direct == 1: x=-1;y=0      #up 
    if direct == 2: x=1;y=0       #down

    newx=x1+x
    newy=y1+y
    ret = ()
    if(newx >len(mat[1])-1 or newy > len(mat[1])-1): ret = False
    elif(mat[newx][newy]!=0): ret = False
    else: ret = (newx,newy)
    return ret

def move(x1,y1,x2,y2,mat,turn=1):
    mat[x1][y1] = 0
    mat[x2][y2] = turn   # catch and excape move differ
    return mat

def catch(mat,day,node_obj):
    node_dict = get_target_position(mat,1)
    if len(node_obj) == 0:
		#in this process the class object node has linked with board matrix by x,y position
		for k,v in node_dict.items(): node_obj[k] = unit(chr(64+k),day,v[0],v[1])    

    print "Energy level: " + ' '.join([str(x.Energy) for x in node_obj.values()])
    #Here the high energy level unit can choose to generate a son, which decrease its energy level but improve its hunting capability.
    for k,v in node_obj.items():
    	if v.Energy > 100 and randint(1,5) > 4: 
    		for direction in range(1,5):
    			ret =  can_move([v.x,v.y],direction,mat)
    			if ret:
    				son = unit(v.Group,day,ret[0],ret[1])
    				node_obj[son.ID] = son
    				mat[ret[0]][ret[1]] =  1
    				node_dict = get_target_position(mat,1)
    				v.Energy -= 40
    				break
	#Here units of lower than 0 energy level should die, what about the key of obj_dict?
    			
    for index in range(1,len(node_dict)):
    	select = node_dict[index]
    	dist_1 = dist(select,mat,2)
	if len(dist_1.values())==0: break
	before_move_dist = min(dist_1.values())
#def try_direction(select,dist_1,turn=2)    
    	direction = range(1,5)
    	random.shuffle(direction)
    	for try_dir in direction:
    		ret = can_move(select,try_dir,mat)
		if ret: 
	    		dist_2 = dist(ret,mat,2)
    	    		after_move_dist = min(dist_2.values())
	    		rand_effect = randint(9,11) 
	    		if after_move_dist*rand_effect*0.1 < before_move_dist: 
					mat = move(select[0],select[1],ret[0],ret[1],mat)
					for k,v in node_obj.items():
						if [v.x,v.y] == select:
							v.x = ret[0]
							v.y = ret[1]
							v.Energy -=  1
					break
    
    #node_dict = get_target_position(mat,1)
    #for v in node_dict.values():print v[0],v[1]
    #for obj in node_obj.values(): print obj.x,obj.y
    mat,node_obj = get_food(mat,node_obj)
    mat = output(mat,2)
    return (mat,node_obj)

def food_move(mat):
    node_dict = get_target_position(mat,2)
    if len(node_dict) < 2: 
	mat = new_food(mat)
    	node_dict = get_target_position(mat,2)

    direct = random.randint(1,4)
    select = node_dict[random.randint(1,len(node_dict))]
    x=select[0]; y=select[1]

    ret = can_move(select,direct,mat)
    if ret: mat = move(x,y,ret[0],ret[1],mat,2)

    mat = output(mat,1)
    return mat

def direct_2pt(x1,y1,x2,y2):
	hori=x1-x2; vert=y1-y2
	x = abs(hori); y = abs(vert)
	if hori != 0 and vert != 0: direct = [hori/x,vert/y]
	elif vert != 0: direct= [x,vert/y]
	elif hori != 0 : direct = [hori/x,y]
	else: direct = [x,y]
	print direct
	return direct

def dist_2pt(x1,y1,x2,y2):
	hori=x1-x2; vert=y1-y2
	x = abs(hori); y = abs(vert)
	dist = x + y 
	return dist

def dist(posi,mat,turn):
    node_dict = get_target_position(mat,turn)
    dist = {}

    for k,v in node_dict.items():
    	hori=v[0]-posi[0]; vert=v[1]-posi[1]
    	x = abs(hori); y = abs(vert)
    	dist[k] = x + y 

    return dist

def get_target_position(mat,turn): # turn standards for role, 1 or 2
    node_dict = {}; i=1

    for xi in range(len(mat[1])):
        for yi in range(len(mat[1])):
            if mat[xi][yi] == turn: 
                node_dict[i] = [xi,yi]
                i += 1
    
    return node_dict

def get_food(mat,node_obj):
    dead = False
    node_dict = get_target_position(mat,2)
    for v in node_dict.values():
            xi = v[0]; yi = v[1]
            if xi<len(mat[1]) -1: f1 = mat[xi+1][yi] * mat[xi][yi]
            else: f1 = 2
            if yi<len(mat[1]) -1: f2 = mat[xi][yi+1] * mat[xi][yi]
            else: f2 = 2
            if xi>0: f3 = mat[xi-1][yi] * mat[xi][yi]
            else: f3 = 2
            if yi>0: f4 = mat[xi][yi-1] * mat[xi][yi]
            else: f4 = 2

            if [f1,f2,f3,f4].count(2) > 1: 
                dead = True
            if dead:
                mat[xi][yi] = 0
                node_obj[2].Energy += 10
                node_obj[2].save_catch_shape(node_obj)
                dead = False

    return (mat,node_obj)

def time(mat,year):
	node_obj={}
	for day in range(year*365):
		mat,node_obj= catch(mat,day,node_obj)
		mat = food_move(mat)

# ________main()_______
mat = _int_(32,32)
time(mat,2)












