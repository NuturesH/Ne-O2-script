#-*-coding:utf-8-*-
#Nutures
#2018/6/5
#extract Overlap and conversion it from diagonal matrix
import os
import numpy as np
import pandas as pd
#fist extract Overlap
def extract_overlap(X):
    Overlap_f = X.replace('.log', '_overlap.csv')
    Overlap_f_swp =  X.replace('.log', '.swp')
    print Overlap_f
    gp = "grep -A 140 'Overlap' " + X + ' > ' + Overlap_f
    print gp
    os.system(gp)
    sd = "sed -i s/'D'/'e'/g " + Overlap_f + ' && ' + "sed -i '/Overlap/d' " + Overlap_f + ' && ' + "awk '{$1=\"\";print $0}' " + Overlap_f + ' > ' + Overlap_f_swp
    os.system(sd)
    print sd
    def write_f(X,Y):
        data = open(X).readlines()
        fp = open(Y, 'w')
        for line in data:
            line = line.strip()
            if '.' in line:
                data_list = line.split()
                if len(data_list) < 5:
                    for i in range(5 - len(data_list)):
                        data_list.append(str(0))
                data = ",".join(data_list)
                print >>fp, data
            else:
                continue
        fp.close()
        return 0
    write_f(Overlap_f_swp, Overlap_f)
    r_f = 'rm ' + Overlap_f_swp
    os.system(r_f)
    return Overlap_f
#second conversion diagonal matrix
def converdion_diagonal_matrix(X):
    overlap = extract_overlap(X)
    matrix = overlap.replace('_overlap', 'matrix')
    data = pd.read_table(overlap, header=None,sep = ',')
    df = pd.DataFrame()
    df1 = pd.DataFrame()
    dim = 34
    start = 0
    end = dim - 1
    twice = 34/5 + 1
    col = 0
    for i in range(twice):
        local = data.loc[start:end, 0:5]
        for n in range(5):
            values = map(float, list(local.iloc[:, n]))
            if len(values) < 34:
                for j in range(34 - len(values)):
                    values.insert(0, 0)
            df[col] = values
            col += 1
        start += end - start + 1
        end = start + dim - 5*(i+1) - 1
    df_swp = np.array(df.loc[:, 0:33])
    df_swp += df_swp.T - np.diag(df_swp.diagonal())
    for i in range(len(df_swp)):
        print i
        print len(df_swp)
        df1[i] = df_swp[:, i]
    df1.to_csv(matrix, index = False, sep = ',')
    return 0
#extract_overlap('/home/nutures/workspace/Ne-O2/structure/1/mole.log')
def main(X):
    converdion_diagonal_matrix(X)
main('/home/nutures/workspace/Ne-O2/structure/1/mole.log')