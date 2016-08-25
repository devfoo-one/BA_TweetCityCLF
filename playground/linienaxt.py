import numpy as np

# row_pattern = r'{} & {}    \\ \hline'
row_pattern = r'{} & {} & {} & {} & {} & {} & {}    \\ \hline'

# lines = [
# 'Precision:	micro=0.28601333333333334	macro=0.046622313891999945	weighted=0.5200793542516762',
# 'Recall:		micro=0.28601333333333334	macro=0.008176353579824224	weighted=0.28601333333333334',
# 'F-Measure:	micro=0.28601333333333334	macro=0.011280316347115875	weighted=0.23194878846930708'
# ]

lines = [
'Precision:      micro=0.35315261344915383       macro=0.5852332564546159        weighted=0.6793022248137315',
'Recall:         micro=0.35315261344915383       macro=0.0942241897302833        weighted=0.35315261344915383',
'F-Measure:      micro=0.35315261344915383       macro=0.14248168398856628       weighted=0.3260526531476309',
'Precision:      micro=0.35224439837134364       macro=0.581877721641847 weighted=0.6781745795948337',
'Recall:         micro=0.35224439837134364       macro=0.09384107928893219       weighted=0.35224439837134364',
'F-Measure:      micro=0.35224439837134364       macro=0.14117119828871313       weighted=0.3246935451615021',
'Precision:      micro=0.35262615756945415       macro=0.5831001444783651        weighted=0.6766643452633756',
'Recall:         micro=0.35262615756945415       macro=0.09380823853377353       weighted=0.35262615756945415',
'F-Measure:      micro=0.35262615756945415       macro=0.1419137096279047        weighted=0.3259880083714697',
'Precision:      micro=0.3533403053335802        macro=0.5823073667106794        weighted=0.6810046587277203',
'Recall:         micro=0.3533403053335802        macro=0.09505306405478166       weighted=0.3533403053335802',
'F-Measure:      micro=0.3533403053335802        macro=0.1435392100980409        weighted=0.3264234660601855',
'Precision:      micro=0.3535580149231308        macro=0.588682586480546 weighted=0.678744839437182',
'Recall:         micro=0.3535580149231308        macro=0.09536552755454718       weighted=0.3535580149231308',
'F-Measure:      micro=0.3535580149231308        macro=0.1444167397870397        weighted=0.32629699043096194',
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
