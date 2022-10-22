import numpy as np

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[90m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_target_position(mat, role): 
    node_dict = {}; i=1

    for xi in range(len(mat[1])):
        for yi in range(len(mat[1])):
            if mat[xi][yi] == role: 
                node_dict[i] = [xi,yi]
                i += 1
    
    return node_dict

def can_move(x1, y1, direct, mat):
    if direct == 3: 
        x=0;y=-1        #left 
    if direct == 4: 
        x=0;y=1         #right
    if direct == 1: 
        x=-1;y=0        #up 
    if direct == 2: 
        x=1;y=0         #down

    newx = x1 + x
    newy = y1 + y
    ret = ()
    if (newx < 0 or newy<0 or newx >len(mat[1])-1 or newy > len(mat[1])-1): 
        ret = False
    elif (mat[newx][newy]!=0): 
        ret = False
    else: 
        ret = (newx, newy)
    return ret


def get_food(mat, node_obj):
    node_dict = get_target_position(mat, 2)
    ate = False

    for k, obj in node_obj.items():
        for v in node_dict.values():
            xi, yi = v
            if np.abs(xi - obj.x) + np.abs(yi - obj.y) == 1:
                ate = True
                mat[xi][yi] = obj.role
                obj.pos.append([xi, yi])

    return mat, node_obj, ate

def direct_2pt(x1,y1,x2,y2):
	hori=x1-x2; vert=y1-y2
	x = abs(hori); y = abs(vert)
	if hori != 0 and vert != 0: direct = [hori/x,vert/y]
	elif vert != 0: direct= [x,vert/y]
	elif hori != 0 : direct = [hori/x,y]
	else: direct = [x,y]
	return direct

def dist_2pt(x1,y1,x2,y2):
	hori=x1-x2; vert=y1-y2
	x = abs(hori); y = abs(vert)
	dist = x + y 
	return dist

def get_dist(x, y, mat, role):
    node_dict = get_target_position(mat, role)
    dist = {}

    for k,v in node_dict.items():
    	hori= v[0] - x; vert=v[1] - y
    	x = abs(hori); y = abs(vert)
    	dist[k] = x + y 

    return dist

def color(text):
    return f"{bcolors.OKGREEN}{text}{bcolors.ENDC}"
