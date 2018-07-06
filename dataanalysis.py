# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 12:40:46 2018

@author: jtfl2
"""

import pandas as pd
import math
import progressbar as pb

df = pd.read_table('bdata.20130222.mhci.txt')
specienames = []
data = []
final = []
newmeas = []
sign = []
totallen = len(df)
for i in range(totallen):
    newmeas.append(math.log10(df.iloc[i][5]))
    if df.iloc[i][5] <= 500:
        sign.append('-')
    else:
        sign.append('+')
    if df.iloc[i][0] not in specienames:
        specienames.append(df.iloc[i][0])
    pb.printProgressBar(i, totallen, prefix = 'Name Progress:', suffix = 'Complete', length = 50)
        
df['meas'] = newmeas
df['sign'] = sign       

for s in specienames:
    print('current species: ' + s + '\n')
    mhc = []
    current = df.loc[df['species'] == s]
    currentlen = len(current)
    for i in range(currentlen):
        if current.iloc[i][1] not in mhc:
            mhc.append(current.iloc[i][1])
        pb.printProgressBar(i, currentlen, prefix = 'MHC Progress:', suffix = 'Complete', length = 50)
    for m in mhc:
        length = []
        newcurrent = current.loc[current['mhc'] == m]
        lenlen = len(newcurrent)
        jtotal = 0
        for j in range(lenlen):
            if newcurrent.iloc[j][2] not in length:
                length.append(newcurrent.iloc[j][2])
            pb.printProgressBar(j, lenlen, prefix = 'Peptide Length Progress ' + str(jtotal) + '/' + str(currentlen) + ':', suffix = 'Complete', length = 50)
            jtotal = jtotal + j
        for l in length:
            final.append(newcurrent.loc[newcurrent['peptide_length'] == l])
    

        



