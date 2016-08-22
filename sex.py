def gender (sex='Unknown'):
    if sex is "m":
        sex = ("Male")
    elif sex is "f":
        sex = ("Female")
    print (sex)

gender("m") # Will print Male
gender("f") # Will print Female
gender()    # Will print Unknown
