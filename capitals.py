def getCap():
    dictionary = {  
        "BC": "Victoria",
        "Alberta": "Edmonton"
        "Saskatchewan" "Regina",
        "New Brunswick": "Frederiction",
        "Manitoba": "Winnipeg",
        "Ontario": "Toronto",
        "P.E.I": "Charlottetown",
        "Nova Scotia": "Halifax",
        "New Found Land": "St. John's"
    }
    return dictionary

if __name__ =="__main__":

    counter= 0
    dictionary = getCap()
    for province in dictionary.items():
        input = input ("The province is" {province[0]}, "What is the capital?")

        if input == province[1]:
            print("That's right!!")
            counter += 1
        else:
            print ("Nice try, The answer is", province[1])
            print (f"Current score: {counter}/9")
    print (f"Your score was {counter}/9")
            
