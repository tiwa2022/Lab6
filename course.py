def getNumber(sCourseNumber):
    dictcourse = {
        "CS101": "3004",
        "CS102": "4501",
        "CS103": "6755",
        "NT110": "1244",
        "CM241": "1411"
    }
    return dictcourse[sCourseNumber]

def getProfessorName(sCourseNumber):
    dictcourse = {
        "CS101": "Haynes",
        "CS102": "Alvarado",
        "CS103": "Rich",
        "NT110": "Burke",
        "CM241": "Lee"
    }
    return dictcourse[sCourseNumber]

def getMeetingTime(sCourseNumber):
    dictcourse = {
        "CS101": "8:00am in the morning",
        "CS102": "9:00am in the morning",
        "CS103": "10:00am in the morning",
        "NT110": "11:00am in the morning",
        "CM241": "1:00pm in the afternoon"
    }
    return dictcourse[sCourseNumber]

if __name__ == "__main__":
    scode= input("Please input your course number: ")
    print("Your room number is", getNumber(scode))
    print("Prof", getProfessorName(scode),"will be your instructor")
    print("Your meeting time will be at", getMeetingTime(scode))
else:
    print("Invalid course code")