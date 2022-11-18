
array1 = [7,5,10,14,3,9,7]
array2 = [9,10,3,4,2,5,7,1]

print("len Array1 :", len(array1))
print("len Array2 :", len(array2))

array1.insert(0,15)
print(" array 1 :  ",array1)
print(" array 2 :  ",array2)

array1.append(1)
array2.append(14)

arrayC = array1.copy()

arrayC.extend(array2)

num7 = 0
for s in arrayC:
    if s == 7:
        num7 += 1 
print("Number in array :", num7)

arrayC.sort()
print(arrayC)

arrayC.remove(7)
arrayD = arrayC.copy()

arrayD.reverse()
print("arr 3 :", (arrayC))
print("arr 4 :", (arrayD))