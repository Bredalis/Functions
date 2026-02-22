
# Example of set usage
names_1 = {"Juan", "Pedro", "Juan", "Pedro"}
names_2 = {"Luis", "Maria", "Rosa"}

print("Sets:", names_1, names_2)
print("Types:", type(names_1), type(names_2))

# Add elements
names_1.add("Luis")
names_2.add("Jose")

# Remove an element
names_2.remove("Luis")

# Union of sets
names = names_1.union(names_2)

print("\nSet 2:", names_2)
print("Union of sets:", names)

# Set operations
both_names = names_1.intersection(names_2)
print("\nCommon data in sets:", both_names)

without_duplicates = names.difference(both_names)
print("Data not repeating in sets:", without_duplicates)

print("\nIs it a subset?:", names_2.issubset(names))
print("Is it a superset?:", names.issuperset(names_2))
