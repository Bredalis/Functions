
# Filter ages less than or equal to 18
ages = [1, 12, 19, 30, 23, 35, 11]
minor_ages = list(filter(lambda x: x <= 18, ages))

print(f"Ages less than or equal to 18: {minor_ages}")
