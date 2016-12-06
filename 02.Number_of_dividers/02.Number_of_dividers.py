# -*- coding: utf-8 -*-
while True:
    number = 0
    dividers = 0
    divider = 0
    try:
        scope = int(input("Please enter scope where I have find number with the greatest number of dividers.'Enter'."))
        if scope > 0:
            for i in range(1,scope+1):
                for z in range(1,i+1):
                    if i % z == 0:
                        divider += 1
                        if divider > dividers:
                            dividers = divider
                            number = i
                divider = 0
            print("Number ", number, " has the greatest number of dividers which is ", dividers)
        else:
            print("Please enter number greater then 0")
        break

    except ValueError:
        print("please enter an integer!")