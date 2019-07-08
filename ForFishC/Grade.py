while True:
    grade = int(input("Please input the Grade: "))
    if grade >= 90:
        print("A")
    else:
        if grade >= 80:
            print("B")
        else:
            if grade >= 60:
                print("C")
            else:
                print("D")
