for i in range(0, 11):
    if i % 2 == 0:
        print(i)


def even(number):
    """
    :param number:
    :return: even number
    """
    x = []
    for ii in range(0, number + 1):
        if ii % 2 == 0:
            x.append(ii)
    return x


list = ['a', 'b', 'v', 'd']
for index, word in enumerate(list):
    print(word + " :" + str(index))
print(even(12))
