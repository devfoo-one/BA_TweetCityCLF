import sys
from Dataset import Dataset

dataset_path = sys.argv[1]
dataset = Dataset(dataset=dataset_path)

# data, targets = dataset.getData(cut_long_tail=False)
# data_NLT, targets_NLT = dataset.getData(cut_long_tail=True)
# names_list = dataset.__target_names_list__
# names_list_nlt = dataset.__target_names_list_noLongTail__
#
# for d, t, dnlt, tnlt, nl, nl_nlt in zip(data, targets, data_NLT, targets_NLT, names_list, names_list_nlt):
#     print(
#         'd_place_id:', d['place']['id'],
#         't:', t,
#         'd_place_name:', d['place']['name'],
#         'ds_query_name:', dataset.getTargetName(t),
#         'dnlt_place_id:', dnlt['place']['id'],
#         'tnlt:', tnlt,
#         'ds_nlt_query_name:', dataset.getTargetName(tnlt),
#         'name_list:', nl,
#         'name_list_nlt', nl_nlt
#     )

# raw_test_data_nlt, test_targets_nlt = dataset.getData(offset=len(dataset) * 0.8, n=len(dataset) * 0.1, cut_long_tail=True)
# test_target_names = [dataset.getTargetName(x) for x in test_targets_nlt]
# for t in set(test_targets_nlt):
#     print(t, dataset.getTargetName(t), 'N =', test_targets_nlt.count(t))

# for i in range(0,10):
#     print('RUN', i)
#     dataset = Dataset(dataset=dataset_path)
#     dataset2 = Dataset(dataset=dataset_path)
#     dataset3 = Dataset(dataset=dataset_path)
#     for a,b,c in zip(dataset.getData(cut_long_tail=True)[1],dataset2.getData(cut_long_tail=True)[1],dataset2.getData(cut_long_tail=True)[1]):
#         if a != b:
#             print(a,b)
#         if b != c:
#             print(b,c)