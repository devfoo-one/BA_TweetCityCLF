import numpy as np

# row_pattern = r'{} & {}    \\ \hline'
row_pattern = r'{} & {} & {} & {} & {} & {} & {}    \\ \hline'

# lines = [
# 'Precision:	micro=0.28601333333333334	macro=0.046622313891999945	weighted=0.5200793542516762',
# 'Recall:		micro=0.28601333333333334	macro=0.008176353579824224	weighted=0.28601333333333334',
# 'F-Measure:	micro=0.28601333333333334	macro=0.011280316347115875	weighted=0.23194878846930708'
# ]

lines = [
'Precision:      micro=0.5986670660476262        macro=0.49243747673940425       weighted=0.6230158545139863',
'Recall:         micro=0.5986670660476262        macro=0.256730849707539 weighted=0.5986670660476262',
'F-Measure:      micro=0.5986670660476262        macro=0.2937287266744421        weighted=0.5726402583332444',
'Precision:      micro=0.5977468588414558        macro=0.5046659203917282        weighted=0.6254565129364915',
'Recall:         micro=0.5977468588414558        macro=0.2567795532032522        weighted=0.5977468588414558',
'F-Measure:      micro=0.5977468588414558        macro=0.293746561702227 weighted=0.5708108834458995',
'Precision:      micro=0.5994109646578795        macro=0.5094059636053115        weighted=0.6270143414774166',
'Recall:         micro=0.5994109646578795        macro=0.26088759270641576       weighted=0.5994109646578795',
'F-Measure:      micro=0.5994109646578795        macro=0.2971435403610079        weighted=0.5733680030883951',
'Precision:      micro=0.5992934594965148        macro=0.500210606103715 weighted=0.6238422713666396',
'Recall:         micro=0.5992934594965148        macro=0.2564673136949232        weighted=0.5992934594965148',
'F-Measure:      micro=0.5992934594965148        macro=0.29337630500333267       weighted=0.5733502336482765',
'Precision:      micro=0.6001251940507787        macro=0.49739541601699044       weighted=0.6256706381749365',
'Recall:         micro=0.6001251940507787        macro=0.2573830978466274        weighted=0.6001251940507787',
'F-Measure:      micro=0.6001251940507787        macro=0.29387582569836507       weighted=0.5740396614137852',
]

scores = {
    'Precision': [],
    'Recall': [],
    'F-Measure': []
}

for l in lines:
    name = l.split()[0][:-1]
    weighted_score = l.split()[3][9:]
    weighted_score = round(float(weighted_score), 5)
    scores[name].append(weighted_score)

for k,v in scores.items():
    mean = round(np.mean(v), 5)
    print(row_pattern.format(k, v[0],v[1],v[2],v[3],v[4], mean))

# for l in lines:
#     name = l.split()[0][:-1]
#     micro_score = l.split()[1][6:]
#     macro_score = l.split()[2][6:]
#     weighted_score = l.split()[3][9:]
#     weighted_score = round(float(weighted_score), 5)
#     line = row_pattern.format(name, weighted_score)
#     print(line)
#     # print(name, micro_score, macro_score, weighted_score, sep="|")
