# printing items from the dictionary
D = {"Roll No.": [1, 2, 3, 4, 5], "Name": ["Ram", "Syam", "Hari", "Sita", "Gita"]}
print(D)
print(D["Roll No."])
print(D["Name"][3])


# Another examples of dictionary
p = {1: "2", True:3, 5.25:False, None:"haha", "a":3.45, 5:{1, 2, 3, 4}, "D":("a",  "z")}
print(P)
# But this dictionary is not actually a dictionary {[1, 2]: "d", "b": 2, (1, 3, 4): 2, {1, 2}: True}
# That means list, tuple and set can not be regarded as the key of the dictionary but they could be regarded as the value of a key
def exchanging_Key_and_value(InDictionary):
    New_Dictionary = {}
    for Key in InDictionary:
        Value = InDictionary[Key]
        try:
            New_Dictionary[Value] = Key
        except:
            print("Value is not suitable as key")
    return New_Dictionary


# It will produce actual new dictionary
print(exchanging_Key_and_value({1: None, False: 'b', 3: 'c'}))

# It will not produce a new dictionary because the formed new dictionary is valid and goes to exception condition
# It will produce only the valid part of the new formed dictionary
print(exchanging_Key_and_value({1: [1, 2, 3], False: 'b', 3: 'c'}))




# Printing the name of the students when the roll no. is entered
a = int(input("Enter the Roll No."))
for i in range(len(D['Roll No.'])):
    if D['Roll No.'][i] == a:
        temp = i
print(D["Name"][temp])
# Another way
A = D["Roll No."]
B = D["Name"]
a = int(input("Enter the Roll No."))
if a == 1:
    print(B[0])
elif a == 2:
    print(B[1])
elif a == 3:
    print(B[2])
elif a == 4:
    print(B[3])
elif a == 5:
    print(B[4])
else:
    print("Invalid Roll No.")

# Adding both keys and values in the dictionary And printing them separately
DS = {"Roll No.": [1, 2, 3, 4, 5], "Name": ["Ram", "Syam", "Hari", "Sita", "Gita"]}
print(DS)
DS["Age"] = ["A", "B", "C", "D", "E"]
print(DS)
for i, j in DS.items():  # To print both keys and values
    print(i, j)
for i in DS.keys():  # To print Keys only
    print(i)
for i in DS.values():  # To print values only
    print(i)

# To delete items
DN = {"Roll No.": [1, 2, 3, 4, 5], "Name": ["Ram", "Syam", "Hari", "Sita", "Gita"]}
del(DN["Roll No."][0])
print(DN)
del(DN["Roll No."][2])
print(DN)
del(DN["Roll No."])
print(DN)

# Adding a dictionary into another dictionary
M1 = {"Ram": 3.65, "Shyam": 3.67}
M2 = {"Sita": 3.78, "Gita": 3.75}
M1.update(M2)
print(M1)

# Adding multiple dictionary into another dictionary
D1 = {"G": 18, "A": 19}
D2 = {"S": 17, "N": 15}
D3 = {}
for i in (D1, D2):
    D3.update(i)
print(D3)

# Merging dictionary
d1 = {"a": 100, "b": 200}
d2 = {"x": 100, "y": 200}
d = d1.copy()
d.update(d2)
print(d)

# Checking key is present or not in the dictionary
D = {"G": 18, "A": 19}
if "G" in D:
    print("Present")
else:
    print("Not present")
if "D" in D:
    print("Present")
else:
    print("Not present")

# Printing key and its value(value should be square of the key) in an empty dictionary
G = {}
for i in range(1, 6):
    G[i] = i ** 2
print(G)

# Create a dictionary, add data like, roll no, name, marks,along with gender, now i want to print all the
# names and marks whose gender is male, how would you do that?
# Print only male data for if you are male print only female data if you are female
R = int(input("inter the roll no."))
Data = {"Roll No.": [1, 2, 3, 4, 5], "Name": ["Shirsak", "Anuragh", "Gauri", "Bikesh", "Jhamputali"], "Marks": [8, 7, 7, 9, 6], "Gender": ["M", "M", "M", "M", "F"]}
for i in range(len(Data["Roll No."])):
    if Data["Roll No."][i] == R:
        temp = i
if Data["Gender"][temp] != "F":
    print(Data["Name"][temp], Data["Marks"][temp], Data["Gender"][temp])
# Another Way(prints all)
Data = {"Roll No.": [1, 2, 3, 4, 5], "Name": ["Shirsak", "Anuragh", "Gauri", "Bikesh", "Jhamputali"], "Marks": [8, 7, 7, 9, 6], "Gender": ["M", "M", "M", "M", "F"]}
for i in range(len(Data["Roll No."])):
    if Data["Gender"][i] == "M":
        print((Data["Name"][i], Data["Marks"][i], Data["Gender"][i]))


# Sorting the keys and the values of the dictionary by ascending and descending
x = {"John": 18, "Ram": 25, "Ama": 34, "Don": 26, "john": 19, "don": 23, "ama":30, "ram": 28}

# ASCENDING:
# Sorting and printing the keys of the dictionary
print(sorted(x))
print(sorted(x.keys()))
# Sorting and printing the values of dictionary
print(sorted(x.values()))
# Sorting and printing the keys of the dictionary along with the values
print(sorted(x.items()))
print(sorted(x.items(), key=lambda x: x[0]))
# Sorting and printing the values of the dictionary along with the keys
print(sorted(x.items(), key=lambda x: x[1]))

# DESCENDING:
# Sorting and printing the keys of the dictionary
a = []
for i in x.keys():
    a.append(i)
print(sorted(a, reverse=True))
# Sorting and printing the values of the dictionary
b =[]
for j in x.values():
    b.append(j)
print(sorted(b, reverse=True))
# Sorting and printing the keys of the dictionary along with the values
print(sorted(x.items(), key=lambda x: x[0], reverse=True))
# Sorting and printing the values of the dictionary along with the keys
print(sorted(x.items(), key=lambda x: x[1], reverse=True))


