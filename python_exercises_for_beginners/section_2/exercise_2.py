# 18.05.24. Sergii Logosha sergiilogosha@gmail.com

strings = ["Hello", "Pizza", "", "World"]
indexes = [2, 4, 3, 15]

for string in strings:
    for index in indexes:
        if (len(string) - 1) < index:
            print("Index out of range")
        elif len(string) == 0:
            print("Empty String")
        else:
            print(string[index])
