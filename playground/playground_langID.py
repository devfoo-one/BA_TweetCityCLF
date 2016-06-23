import json, langid

count_all = 0
count_realDe = 0
with open('../../data/Germany_filtered.json') as dataset:
    for line in dataset:
        text = json.loads(line)['text']
        lang, score = langid.classify(text)
        count_all += 1
        if lang == 'de':
            # print(lang, '\t', score, '\t\t\t', text)
            count_realDe += 1
        if count_all % 1000 == 0:
            print(count_all, count_realDe, (count_realDe * 100 / count_all))


