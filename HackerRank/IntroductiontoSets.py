def average(array):
    myset = set()

    for i in range(len(array)):
        myset.add(array[i])

    return sum(myset)/float(len(myset))




print(average([161, 182, 161, 154 ,176 ,170, 167, 171 ,170, 174]))
