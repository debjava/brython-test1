def getFullName(firstName, lastName):
    return firstName + lastName

def sayHello():
    print("Hello")
    return "Hello World"

def sayHi(param1):
    print("Hello")
    return param1 + " Hello World"

if __name__ == '__main__':
    someValue = sayHello()
    print("Some Value: ", someValue)
    print("Passed param: ", sayHi("DD"))