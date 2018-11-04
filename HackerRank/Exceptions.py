# try:
#     print(1//0)
# except ZeroDivisionError as e:
#     print(e)

t = int(input())

for i in range(t):
    val = input().split(" ")

    try:
        print(round(int(val[0])//int(val[1])))
    except ZeroDivisionError as e:
        print("Error Code: " + str(e))
    except ValueError as e:
         print("Error Code: " + str(e))