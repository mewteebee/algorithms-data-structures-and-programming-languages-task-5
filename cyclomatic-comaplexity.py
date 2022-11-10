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
    print(average, "Class Average")


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
    print(round(average, 1), "Class Average")
    print(((passes / len(grades)) * 100), "Pass Rate")


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
