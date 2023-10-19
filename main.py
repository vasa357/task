import random
student_number = 1
count = 10 + student_number
random_numbers = [random.randint(30, 90) for _ in range(count)]
print(random_numbers)