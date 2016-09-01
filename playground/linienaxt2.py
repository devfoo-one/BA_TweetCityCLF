import numpy as np

# row_pattern = r'{} & {} & {} & {} & {} & {} & {}    \\ \hline'
row_pattern = r'\textbf{{{}}} & {:1.3f} & \(\pm\) {:1.4f} & {:1.3f} & \(\pm\) {:1.4f} \\'
row_pattern_accuracy = r'\textbf{{Accuracy}} & {:1.3f} & \(\pm\) {:1.4f} & \\'

lines = [
'Precision:      micro=0.28424341265006975       macro=0.03905690479533423       weighted=0.5139105005277206',
'Recall:         micro=0.28424341265006975       macro=0.00699301457743636       weighted=0.28424341265006975',
'F-Measure:      micro=0.28424341265006975       macro=0.009626869218055533      weighted=0.2308581258530854',
'Accuracy:       0.28424341265006975',
'Precision:      micro=0.2880348633244386        macro=0.05166217571347683       weighted=0.5271563159251297',
'Recall:         micro=0.2880348633244386        macro=0.009329320989420908      weighted=0.2880348633244386',
'F-Measure:      micro=0.2880348633244386        macro=0.012918121192202956      weighted=0.23510776933664634',
'Accuracy:       0.2880348633244386',
'Precision:      micro=0.29011037461233613       macro=0.05647456570424138       weighted=0.5293321603526603',
'Recall:         micro=0.29011037461233613       macro=0.010053400919844543      weighted=0.29011037461233613',
'F-Measure:      micro=0.29011037461233613       macro=0.01393946762736545       weighted=0.23702951521418106',
'Accuracy:       0.29011037461233613',
'Precision:      micro=0.291389359470797 macro=0.06275684934960865       weighted=0.5401565953956473',
'Recall:         micro=0.291389359470797 macro=0.011299726897720441      weighted=0.291389359470797',
'F-Measure:      micro=0.291389359470797 macro=0.015583649691314944      weighted=0.23860316201068127',
'Accuracy:       0.291389359470797',
'Precision:      micro=0.2929391247921483        macro=0.06648154584185603       weighted=0.5398953762182738',
'Recall:         micro=0.2929391247921483        macro=0.011596993306557331      weighted=0.2929391247921483',
'F-Measure:      micro=0.2929391247921483        macro=0.01617484270980137       weighted=0.23963631904582605',
'Accuracy:       0.2929391247921483',
]

scores = {
    'Precision': {'macro': [], 'weighted': []},
    'Recall':  {'macro': [], 'weighted': []},
    'F-Measure':  {'macro': [], 'weighted': []},
    'Accuracy': []
}
#
for l in lines:
    name = l.split()[0][:-1]
    if name == 'Accuracy':
        scores[name].append(float(l.split()[1]))
        continue
    macro_score = l.split()[2].split(sep='=')[1]  # macro
    weighted_score = l.split()[3].split(sep='=')[1]  # weighted
    scores[name]['macro'].append(float(macro_score))
    scores[name]['weighted'].append(float(weighted_score))

for k in ['Precision','Recall', 'F-Measure', 'Accuracy']:
    v = scores[k]
    if k == 'Accuracy':
        print(r'\midrule')
        mean = np.mean(v)
        std = np.std(v)
        print(row_pattern_accuracy.format(mean, std))
        continue
    macro_mean = np.mean(v['macro'])
    macro_std = np.std(v['macro'])
    weighted_mean = np.mean(v['weighted'])
    weighted_std = np.std(v['weighted'])
    if k == 'F-Measure':
        k = 'F-Maß'
    print(row_pattern.format(k, macro_mean, macro_std, weighted_mean, weighted_std))
