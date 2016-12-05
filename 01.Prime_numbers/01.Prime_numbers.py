## -*- coding: utf-8 -*-
while True:
    try:
        rangex = int(input("Please enter numeric range in which I have to find prime numbers. 'Enter'."))
        if rangex > 1:
            for i in range(2,rangex+1):
                for z in range(2,i):
                    if i % z == 0:
                        break
                else:
                    print(i, "is a prime number.")
        else:
            print("Please enter number greater than 1.")
        break

    except ValueError:
        print("Please enter an integer!")

#





