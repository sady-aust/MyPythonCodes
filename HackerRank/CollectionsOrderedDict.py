# from collections import OrderedDict
#
# myOrderDict = OrderedDict();
# myOrderDict["a"] = 1
# myOrderDict["c"] = 2
# myOrderDict["b"] = 3
# myOrderDict["d"] = 4
# myOrderDict["c"] = 4
#
# print(myOrderDict)

from collections import OrderedDict

n = int(input())

myOrderDict = OrderedDict()

for i in range(n):
    myIn = input().split(" ")

    product = ""
    for j in range(len(myIn) - 1):
        product += (myIn[j] + " ")

    product = product.strip()

    if myOrderDict.__contains__(product):
        myOrderDict[product] = myOrderDict[product]+int(myIn[len(myIn)-1])
    else:
        myOrderDict[product] = int(myIn[len(myIn)-1])

for item in myOrderDict:
   ans = str(item)+" "+str(myOrderDict[item])
   print(ans)