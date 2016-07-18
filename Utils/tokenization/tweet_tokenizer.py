import re

class Tokenizer:
    def __call__(self, t):
        t = str(t)
        links_re = re.compile('http[s]?://\S+')
        split_re = re.compile('[\s\r\n\.,\?!]+')
        links = links_re.findall(t)  # exctract links
        for l in links:
            t = t.replace(l, '')
        return split_re.split(t) + links  # add unmodified links
