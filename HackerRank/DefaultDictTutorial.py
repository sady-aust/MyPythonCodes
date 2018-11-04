# from collections import defaultdict
# d = defaultdict(list)
# d["python"].append("awesome")
# d["something-else"].append("not relevent")
# d["python"].append("language")
#
# print(d["Java"])

from collections import defaultdict

nm = input().split(" ")
d = defaultdict(list)

for i in range(int(nm[0])):
    word = input()
    d[word].append(i+1)

for i in range(int(nm[1])):
    q = input()
    if not d.__contains__(q):
        print("-1")
    else:
        ansList = d[q]
        ansString = ""
        for item in ansList:
            ansString += (str(item)+" ")

        print(ansString.strip())
