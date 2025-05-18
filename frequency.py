x = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 10}

y = int(input("Enter the value to check frequency: "))


z = sum(1 for value in x.values() if value == y)

print(f"Frequency of {y}: {z}")