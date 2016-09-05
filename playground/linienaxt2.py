import numpy as np

# row_pattern = r'{} & {} & {} & {} & {} & {} & {}    \\ \hline'
row_pattern = r'\textbf{{{}}} & {:1.3f} \(\pm\) {:1.4f} & {:1.3f} \(\pm\) {:1.4f} \\'
row_pattern_accuracy = r'\textbf{{Accuracy}} & \multicolumn{{2}}{{c}}{{{:1.3f} \(\pm\) {:1.4f}}} \\'

lines = [
'Precision:      micro=0.33461135240377415       macro=0.35447043524383304       weighted=0.6140031493693543',
'Recall:         micro=0.33461135240377415       macro=0.06106796581903504       weighted=0.33461135240377415',
'F-Measure:      micro=0.33461135240377415       macro=0.08866456325020579       weighted=0.30027332352269615',
'Accuracy:       0.33461135240377415',
'Precision:      micro=0.334124347413384 macro=0.3580373105662054        weighted=0.6117087397575096',
'Recall:         micro=0.334124347413384 macro=0.06146452232343936       weighted=0.334124347413384',
'F-Measure:      micro=0.334124347413384 macro=0.08910840966856995       weighted=0.29943560344609493',
'Accuracy:       0.334124347413384',
'Precision:      micro=0.33466507990479427       macro=0.35403222461215766       weighted=0.6111644278378144',
'Recall:         micro=0.33466507990479427       macro=0.06129816063236702       weighted=0.33466507990479427',
'F-Measure:      micro=0.33466507990479427       macro=0.08914235961024705       weighted=0.3008482709795503',
'Accuracy:       0.33466507990479427',
'Precision:      micro=0.33537155924282075       macro=0.3605786678896247        weighted=0.614071363042398',
'Recall:         micro=0.33537155924282075       macro=0.062275704558645985      weighted=0.33537155924282075',
'F-Measure:      micro=0.33537155924282075       macro=0.0904674322649539        weighted=0.30130058775383034',
'Accuracy:       0.33537155924282075',
'Precision:      micro=0.3349141168811658        macro=0.36346638383387436       weighted=0.6159229740733969',
'Recall:         micro=0.3349141168811658        macro=0.06033543723692743       weighted=0.3349141168811658',
'F-Measure:      micro=0.3349141168811658        macro=0.08778365677637785       weighted=0.30014925669189363',
'Accuracy:       0.3349141168811658',
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

print('')
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
        k = 'F1-Maß'
    print(row_pattern.format(k, macro_mean, macro_std, weighted_mean, weighted_std))
