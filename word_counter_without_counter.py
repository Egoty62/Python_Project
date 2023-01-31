from collections import OrderedDict
from collections import defaultdict

text_origin = input("원하는 문장을 입력하여 주십시오 :")
text = text_origin.lower().split()

word_count = defaultdict(lambda : 0)

for word in text :
    word_count[word] += 1

for k, v in OrderedDict(sorted(word_count.items(), key = lambda t : t[1], reverse = True)).items() :
    print(k, v)