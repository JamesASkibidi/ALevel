import random
def random_list(a,b,c):
    list = []
    for i in range(c):
        num = random.randint(a,b)
        list.append(num)

    return list