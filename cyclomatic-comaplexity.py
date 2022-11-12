grades = [19, 20, 45, 89, 68, 73, 96, 100, 92, 43, 22, 27, 55, 40]

# Python program with a cyclomatic complexity of four
def passOrFail(grades):
    for grade in grades:
        if(grade >= 50 and grade <= 100):
            print(grade, "PASS")
        else:
            print(grade, "FAIL")

# Python program with a cyclomatic complexity of five
def passOrFailWithAverage(grades):
    average = sum(grades) / len(grades)
    for grade in grades:
        if(grade >= 50 and grade <= 100):
            print(grade, "PASS")
        else:
            print(grade, "FAIL")
    if(average > 50):
        print(average, "High Performing Class")
    else:
        print(average, "Low Performing Class")

# Python program with a cyclomatic complexity of six
def passOrFailWithAverageAndPassRate(grades):
    passes = 0
    average = sum(grades) / len(grades)
    for grade in grades:
        if(grade >= 50 and grade <= 100):
            print(grade, "PASS")
            passes += 1
        else:
            print(grade, "FAIL")
    passRate = ((passes / len(grades)) * 100)
    if (average > 50):
        print(average, "High Performing Class")
    else:
        print(round(average, 1), "Low Performing Class")
    if(passRate != 0):
        print(passRate, "% of students graduating")

# Python program with a cyclomatic complexity of seven
def gradesCalculator(grades):
    for grade in grades:
        if(grade >= 80):
            print(grade, "A")
        elif(grade >= 70 and grade <= 79):
            print(grade, "B")
        elif(grade >= 60 and grade <= 69):
            print(grade, "C")
        else:
            print(grade, "D")

Program B with cyclomatic complexity of four
def bus(passengers):
    max_cap = 33
    if(passengers > max_cap):
        print(f"{passengers} is too much for a bus")
    elif(passengers < max_cap):
        remaining_seats = max_cap - passengers
        print(f"Bus has taken {passengers} passengers, there are {remaining_seats} empty seats.")
    elif(passengers == max_cap):
        print("The bus is at full capacity!")
    else:
        print("Invalid input")

