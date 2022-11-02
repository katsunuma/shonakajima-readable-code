path = "dictionary-data.txt"

with open(path,encoding="utf-8") as f:
    text = [s.strip() for s in f.readlines()]

length = len(text)

for i in range(length):
    print("{}:{}".format(i+1,text[i]))