import numpy as np

# row_pattern = r'{} & {} & {} & {} & {} & {} & {}    \\ \hline'
row_pattern = r'\textbf{{{}}} & {:1.3f} \(\pm\) {:1.4f} & {:1.3f} \(\pm\) {:1.4f} \\'
row_pattern_accuracy = r'\textbf{{Accuracy}} & \multicolumn{{2}}{{c}}{{{:1.3f} \(\pm\) {:1.4f}}} \\'

lines = [
'Precision:      micro=0.5910089361489691        macro=0.16335007118164732       weighted=0.5599668661148671',
'Recall:         micro=0.5910089361489691        macro=0.09413274017554112       weighted=0.5910089361489691',
'F-Measure:      micro=0.5910089361489691        macro=0.11083103255024725       weighted=0.5308579483527887',
'Accuracy:       0.5910089361489691',
'Precision:      micro=0.5929658032123498        macro=0.16565485295734111       weighted=0.5613921373081544',
'Recall:         micro=0.5929658032123498        macro=0.0966258495042081        weighted=0.5929658032123498',
'F-Measure:      micro=0.5929658032123498        macro=0.11322031451273513       weighted=0.5321301039162746',
'Accuracy:       0.5929658032123498',
'Precision:      micro=0.5944806688401304        macro=0.16339706683191238       weighted=0.5620781929449696',
'Recall:         micro=0.5944806688401304        macro=0.09509227539693207       weighted=0.5944806688401304',
'F-Measure:      micro=0.5944806688401304        macro=0.11166283750022377       weighted=0.5342009408898039',
'Accuracy:       0.5944806688401304',
'Precision:      micro=0.595350443088963 macro=0.17038227970018213       weighted=0.5647520796257235',
'Recall:         micro=0.595350443088963 macro=0.10003984555613035       weighted=0.595350443088963',
'F-Measure:      micro=0.595350443088963 macro=0.11716106646360838       weighted=0.5357978926782929',
'Accuracy:       0.595350443088963',
'Precision:      micro=0.5943312133807401        macro=0.1652534577637222        weighted=0.5641185617198196',
'Recall:         micro=0.5943312133807401        macro=0.0961233117798371        weighted=0.5943312133807401',
'F-Measure:      micro=0.5943312133807401        macro=0.11304760053205629       weighted=0.5350825102552115',
'Accuracy:       0.5943312133807401',
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
