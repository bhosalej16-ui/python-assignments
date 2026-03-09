my_list = [10, 20, 30, 40, 20]
print("Original List:", my_list)

my_list.append(50)
print("After Append:", my_list)

my_list.remove(20)
print("After Remove:", my_list)

print("First Element:", my_list[0])

print()
my_set = {10, 20, 30, 40, 20}

print("Original Set:", my_set)

my_set.add(50)
print("After Add:", my_set)

my_set.remove(10)
print("After Remove:", my_set)

print()

my_tuple = (10, 20, 30, 40)

print("Tuple:", my_tuple)

print("Second Element:", my_tuple[1])

print()

my_dict = {
    "name": "Toast",
    "age": 18,
    "course": "Computer Science"
}

print("Original Dictionary:", my_dict)

my_dict["city"] = "Pune"
print("After Adding City:", my_dict)

print("Name:", my_dict["name"])
my_dict["age"] = 18
print("After Updating Age:", my_dict)