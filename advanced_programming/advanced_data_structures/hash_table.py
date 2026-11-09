def user_hash(key, size):
    #perfrms hask using the value as a key

    key = key

    

    total = 0
    totalMult = 1
    totalSum = 0
    for num in key:
        num = int(num)
        totalSum = totalSum + num
        if num == 0:
            pass
        else:
            totalMult = totalMult * num
        

    hash_val = ((totalMult+totalSum)*num)%size

     

    return hash_val


def reg_hash(key):
    hash = []
    num = 0
    numerical = [None, None, None, None]
    num_loop = 1
    for i in key:

        try:
            int(i)

        except:
            if ord(i) == 32:
                pass
            else:
                hash.append(ord(i))
  
        else:



            i = int(i)
            if num_loop % 2 != 0:
                i = i*10
                numerical[num_loop-1] = i
            else:

                numerical[num_loop - 2] = numerical[num_loop - 2] + i

                num_loop = num_loop +1

        for i in numerical:
            hash.append(i)
        





    for i in hash:
        print(i)

    print(hash)

# key = input('Enter a value: ')
# size = 30

# print(user_hash(key , size))

print(reg_hash("AB72 CDE"))

hashtable = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,

]
