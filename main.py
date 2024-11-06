import random
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array)

# výměna čísla v poli
array[5] = 8
print(array)

#Délka pole
lenarray = len(array)
print(lenarray)
#Druhé pole
arraya = [6, 8, 9, 4, 15, 58, 2, 3, 1, 7]
print(sum(arraya + array))

array_random=list(range(1,51)) # Random 
random.shuffle(array_random)
print (array_random)