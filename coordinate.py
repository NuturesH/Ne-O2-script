#-*-coding:UTF-8-*-
#Nutures

# randomly generated pdb structure
import math
import numpy as np

def random_coordinate(X):
    Ne_list = []
    Ne_len = len(Ne_list)
    while Ne_len < 1:
        Ne = [np.random.uniform(-10, 10) for i in range(3)]
        Ne_a = np.array(Ne)
        O_Ne_bond = np.linalg.norm(X - Ne_a)
        if O_Ne_bond < 5 and Ne not in Ne_list:
            Ne_list.append(Ne)
            Ne_len = len(Ne_list)
            print Ne, O_Ne_bond
            continue
        else:
            Ne_len = len(Ne_list)
            continue
    return  Ne_list

#write_line
def write_line(X, Y):
    coord = str(X[0]) + '  ' + str(X[1]) + '  ' + str(X[2])
    if atom == 'Ne':
        #print " ".join(X)
        line = 'ATOM' + "   " + str(num) + " " + atom + "       " + str(0) + "      " + coord  + '       ' + atom
    else:
        line = 'ATOM' + "   " + str(num) + "  " + atom + "       " + str(0) + "      " + coord   + '        ' + atom
    return line

#write pdb
def write_pdb():
    roots = '../structure/'
    O_Coord = [0.976, 0.154, -1.021]
    #model = []
    model_pdb = open('./model/mole.pdb').readlines()
    for i in range(1,1101):
        file_name = roots + str(i) + '/' + 'mole.pdb'
        print file_name
        fp = open(file_name, 'w')
        Ne_list = []
        while len(Ne_list) < 1:
            Ne_Coord = [round(np.random.uniform(-10, 10), 3) for i in range(3)]
            Ne_array = np.array(Ne_Coord)
            def bond(X, Y):
                k = math.sqrt((X[0]-Y[0])*(X[0]-Y[0]) + (X[1]-Y[1])*(X[1]-Y[1]) + (X[2]-Y[2])*(X[2]-Y[2]))
                return k
            O_NE_bond = bond(O_Coord, Ne_Coord)
            if O_NE_bond < 5 and O_NE_bond > 2:
                print O_NE_bond
                Ne_list.append(Ne_Coord)
                print Ne_Coord
                continue
            else:
                continue
        for line in model_pdb:
            if 'Ne' in line:
                if Ne_Coord[0] < 0:
                    line = line.replace(' 2.018', str(Ne_Coord[0]))
                else:
                    line = line.replace('2.018', str(Ne_Coord[0]))
                if Ne_Coord[1] < 0:
                    line = line.replace(' 1.789', str(Ne_Coord[1]))
                else:
                    line = line.replace('1.789', str(Ne_Coord[1]))
                if Ne_Coord[2] < 0:
                    line = line.replace(' 0.541', str(Ne_Coord[2]))
                else:
                    line = line.replace('0.541', str(Ne_Coord[2]))
                print >> fp, line.strip()
            else:
                print >> fp, line.strip()
write_pdb()
