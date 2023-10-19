student_number = 5
M = 5
X = [3,-2,6,-8,0,9,12,-4,7,1]
Y = [x for x in X if abs(x) > M]
print("число:", M)
print("масив:", X)
print("масив Y(елемент, що більще за модулем за M):", Y)