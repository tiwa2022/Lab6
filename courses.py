
def getRoom(nCoursenumber):
    dictRoomNumber = {
        "CS101": "3004",
        "CS102": "4501",
        "CS103": "6755",
        "NT110": "1244",
        "CM241": "1411",
    }
    return dictRoomNumber[nCoursenumber]

if __name__ == "__main__":
    nCourse = input ("Pleasr enter your course ")
    print("The room number is", getRoom(nCourse))