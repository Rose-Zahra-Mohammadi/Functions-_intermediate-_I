x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]
# 1.Update Values in Dictionaries and Lists
# a. Change the value 10 in x to 15.
x[1][0] = 15
print(x)

# b. Change the last_name of the first student from 'Jordan' to 'Bryant'

students[0]['last_name'] = 'Bryant'
print(students)

# c. In the sports_directory, change 'Messi' to 'Andres'

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# d.Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# 2.Iterate Through a List of Dictionaries

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(some_list):
    for dictionary in some_list:
        info = ""
        for key in dictionary:
            if key == 'first_name':
                info += f"{key} - {dictionary[key]}, "
            else:
                info += f"{key} - {dictionary[key]}"
        print(info)

iterateDictionary(students)

# 3.Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        for key in dictionary:
            if key == key_name:
                print(dictionary[key])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 4.Iterate Through a Dictionary with List Values
dojo = {'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        KEY = key.upper()
        print(str(len(some_dict[key])) +" " + KEY)
        for e in some_dict[key]:
            print(e)

printInfo(dojo)