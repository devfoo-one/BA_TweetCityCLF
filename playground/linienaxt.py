import numpy as np

# row_pattern = r'{} & {}    \\ \hline'
row_pattern = r'{} & {} & {} & {} & {} & {} & {}    \\ \hline'

# lines = [
# 'Precision:	micro=0.28601333333333334	macro=0.046622313891999945	weighted=0.5200793542516762',
# 'Recall:		micro=0.28601333333333334	macro=0.008176353579824224	weighted=0.28601333333333334',
# 'F-Measure:	micro=0.28601333333333334	macro=0.011280316347115875	weighted=0.23194878846930708'
# ]

lines = [
'Precision:      micro=0.3513553991313464        macro=0.5765617934505769        weighted=0.6762664362928091',
'Recall:         micro=0.3513553991313464        macro=0.09277997499114958       weighted=0.3513553991313464',
'F-Measure:      micro=0.3513553991313464        macro=0.1403276503844492        weighted=0.32358512042817966',
'Precision:      micro=0.350640721404841 macro=0.576684815498224 weighted=0.6750171491712896',
'Recall:         micro=0.350640721404841 macro=0.09282272856508299       weighted=0.350640721404841',
'F-Measure:      micro=0.350640721404841 macro=0.1398088809662211        weighted=0.32234177317607643',
'Precision:      micro=0.3509060543632618        macro=0.5756868629735749        weighted=0.6739621012421979',
'Recall:         micro=0.3509060543632618        macro=0.09245131924345028       weighted=0.3509060543632618',
'F-Measure:      micro=0.3509060543632618        macro=0.13997218499308772       weighted=0.32350489466198895',
'Precision:      micro=0.35170405360100476       macro=0.5839633680067038        weighted=0.679790028224153',
'Recall:         micro=0.35170405360100476       macro=0.09423482564893462       weighted=0.35170405360100476',
'F-Measure:      micro=0.35170405360100476       macro=0.1426045162925874        weighted=0.3240026954834392',
'Precision:      micro=0.3516300265411388        macro=0.5864030308667121        weighted=0.6767186791253311',
'Recall:         micro=0.3516300265411388        macro=0.09460174142201007       weighted=0.3516300265411388',
'F-Measure:      micro=0.3516300265411388        macro=0.1434445354311343        weighted=0.3235957113806251',
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
