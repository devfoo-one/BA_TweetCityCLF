import json

country_code_counter = {}
i = 0
with open('../../data/Germany_filtered_shuffled.json') as jsonfile:
    for line in jsonfile:
        tweet = json.loads(line)
        country_code = tweet['place']['country_code']
        if country_code not in country_code_counter.keys():
            country_code_counter[country_code] = 0
        country_code_counter[country_code] += 1
        i += 1
        if i % 100000 == 0:
            print(i)

print(sorted(country_code_counter.items(), key=lambda x: x[1], reverse=True))