import collections

# Point = collections.namedtuple('Point','x,y')
# pt1 = Point(1,2)
# pt2 = Point(3,4)
#
# dot_product = (pt1.x*pt2.x)+(pt1.y*pt2.y)
# print(dot_product)


# Car = collections.namedtuple("Car","Price Mileage Color Class")
# xyz = Car(Price=100000,Mileage=30,Color="Red",Class="Y")
#
# print(xyz.Class)

n = int(input())
order = input().split(" ")
myOrder = list()

for item in order:
    if not item.__eq__(""):
        myOrder.append(item)

Student = collections.namedtuple("Student", "ID,MARKS,NAME,STUDENT,CLASS")

total = 0
for i in range(n):
    rowData = input().split(" ")
    data = list()

    for item in rowData:
        if not item.__eq__(""):
            data.append(item)

    total += int(data[myOrder.index("MARKS")])



print(total/n)