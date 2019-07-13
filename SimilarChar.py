stringSize = int(input())
string = input()
queries = int(input())

while queries != 0:
    q = int(input())
    myString = string[:q]
    print(myString)
    print(myString.count(myString[q-1]) - 1)

    queries -= 1

