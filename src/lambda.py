
# Anonymous functions (Lambda)

addition = (lambda a, b: a + b)
multiplication = (lambda a, b, c: a * b * c)
constant = (lambda x: x)

people_data = [("Juan", 89, 5), ("Lucía", 45, 10), ("Pedro", 23, 30)]

print("Data structure:")
print("Unsorted list:", people_data)

# Sort the list of people by the second position (age)
people_data.sort(key=lambda person: person[1])
print("Sorted list:", people_data)

print("\nOperations:")
print("Addition:", addition(2, 3))
print("Multiplication:", multiplication(1, 2, 3))
print("Constant:", constant(3))
