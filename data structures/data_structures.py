import numpy

#Linked List - dynamic - mutable - heterogenous
scores = [110 , 90 , 4 , 63 , 'fifty']


#tuple - static - immutable - heterogenous
scores_tuple= (110, 90, 4, 63 , 'fifty')

# #dictionary
score_dictionary = {
    'Me': 20,
    'Raff' : 100,
    'pedro' : 0,
    'joe' : 999,
}

#array - static - mutable - homogenous
scores_array = numpy.array([110, 90, 4, 63])
scores_array[0] = 1

print(*scores_tuple)