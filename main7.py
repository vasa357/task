student_number = 11
array_length = 10 + student_number
original_array =[3,-2,6,-8,0,-9,12,-4,7,1]
modified_array =[abs(x) for x in original_array]
print("заданий масив:", original_array)
print("масив після заміни негативних на позитивні:", modified_array)
