import numpy as np

# row_pattern = r'{} & {}    \\ \hline'
row_pattern = r'{} & {} & {} & {} & {} & {} & {}    \\ \hline'

# lines = [
# 'Precision:	micro=0.28601333333333334	macro=0.046622313891999945	weighted=0.5200793542516762',
# 'Recall:		micro=0.28601333333333334	macro=0.008176353579824224	weighted=0.28601333333333334',
# 'F-Measure:	micro=0.28601333333333334	macro=0.011280316347115875	weighted=0.23194878846930708'
# ]

lines = [
'Precision:      micro=0.28424341265006975       macro=0.03905690479533423       weighted=0.5139105005277206',
'Recall:         micro=0.28424341265006975       macro=0.00699301457743636       weighted=0.28424341265006975',
'F-Measure:      micro=0.28424341265006975       macro=0.009626869218055533      weighted=0.2308581258530854',
'Precision:      micro=0.2880348633244386        macro=0.05166217571347683       weighted=0.5271563159251297',
'Recall:         micro=0.2880348633244386        macro=0.009329320989420908      weighted=0.2880348633244386',
'F-Measure:      micro=0.2880348633244386        macro=0.012918121192202956      weighted=0.23510776933664634',
'Precision:      micro=0.29011037461233613       macro=0.05647456570424138       weighted=0.5293321603526603',
'Recall:         micro=0.29011037461233613       macro=0.010053400919844543      weighted=0.29011037461233613',
'F-Measure:      micro=0.29011037461233613       macro=0.01393946762736545       weighted=0.23702951521418106',
'Precision:      micro=0.291389359470797 macro=0.06275684934960865       weighted=0.5401565953956473',
'Recall:         micro=0.291389359470797 macro=0.011299726897720441      weighted=0.291389359470797',
'F-Measure:      micro=0.291389359470797 macro=0.015583649691314944      weighted=0.23860316201068127',
'Precision:      micro=0.2929391247921483        macro=0.06648154584185603       weighted=0.5398953762182738',
'Recall:         micro=0.2929391247921483        macro=0.011596993306557331      weighted=0.2929391247921483',
'F-Measure:      micro=0.2929391247921483        macro=0.01617484270980137       weighted=0.23963631904582605',
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
