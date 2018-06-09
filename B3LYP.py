#-*-coding:utf-8-*-
#Nutures
#2018/5/25
#B3LYP

import re
import os
#write Model file
def mod(X,Y):
    model = []
    for line in open(X):
        line = line.strip()
        if '%chk' in line:
            model.append(Y)
            continue
        else:
            model.append(line)
            continue
    return model

#write Coordinate file
def Coor(X):
    #num = 0
    Coordinate = []
    for line in open(X):
        line = line.strip()
        atom_name = line.split()[-1]
        coor = line[32:56].strip()
        print coor
        if atom_name == 'Ne':
            i = atom_name + '   ' + coor
        else:
            i = atom_name + '    ' + coor
        #i = atom_name + "    " + coor
        if line == 'END':
            #num += 1
            continue
        else:
            Coordinate.append(i)
    Coordinate.append('')
    return Coordinate
#write sh file
def l_sh(X):
    fk = open('./sh/DDTF_gua.sh', 'w')
    num = 0
    for line in open(X):
        numb = re.findall(r'\d+', line)[0] + '/'
        line = line.strip().split('/')[-1]
        gjf = '../../DDTF/' + numb + line.replace('pdb', 'gjf')
        g16 = 'g16 ' + gjf
        chk = gjf.replace('gjf', 'chk')
        fchk = gjf.replace('gjf', 'fchk')
        chk_fchk = 'formchk ' + chk + ' > ' + fchk
        echn = 'echo ' + str(num)
        num += 1
        print >> fk, g16
        print >> fk, chk_fchk
        print >> fk, echn
    fk.close()
    return 0
#write Guassion file
#Y:model file , X:coordinate file
def Guas(X,Y):
    l_sh(X)
    for name in open(X):
        name = name.strip()
        ####
        input_file =  name
        coordinate = Coor(input_file)
        ####
        numb = re.findall(r'\d+', name)[0] + '/'
        line = name.strip().split('/')[-1]
        out_file = '../DDTF/' + numb + line.replace('pdb', 'gjf')
        #out_file = '../tddft/' + name
        fp = open(out_file, 'w')
        ###
        out_file = '../' + out_file
        chk_name = '%chk=' + out_file.replace('gjf','chk')
        model = mod(Y, chk_name)
        # write model to guassion file
        for i in model:
            print >> fp, i
        #write coordinate to guassion file
        for i in coordinate:
            print >> fp, i
        fp.close()
Guas('../raw_data/path_and_name.dat', './model/CCSD.gjf')