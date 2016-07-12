import pickle
import matplotlib.pyplot as plt
import numpy as np

"""load persistent dataset"""
with open('../dataset.pickle', 'rb') as f:
    dataset = pickle.load(f)
sortedTargets = sorted(dataset.__target_counter.items(), key=lambda x: x[1], reverse=True)
count_top = sortedTargets[0][1]
count_total = 0
for target, count in sortedTargets:
    count_total += count
    print('"',dataset.getTargetName(target)[0],'";',count, sep='')
print('total:', count_total, 'first:', count_top, 'baseline:', count_top * 100 / count_total)



# for target, count in sortedTargets:
#     count_total += count
#     plot_targets.append(list(dataset.getTargetName(target))[0])
#     plot_counts.append(count)
# print('total:', count_total, 'first:', count_top, 'baseline:', count_top * 100 / count_total)
#
# y_pos = np.arange(len(plot_targets))
#
# plt.bar(y_pos, plot_targets, plot_counts)
# plt.ylabel('Count')
# plt.xlabel('Target')
# plt.title('Target count in filtered de-dataset')
# plt.show()