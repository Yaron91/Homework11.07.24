while True:
    a: str = input ("Please enter a first phrase: ");
    b: str = input ("Please enter a second phrase: ");

    if a == b:
        print ("Two identical strings... Game over");
        break
    else:
        print(a + " " + b)
