Fodd = []
listing = True
while listing == True:
    command = input("Please enter the command (SHOW/ADD/END). ")
    if command == ("SHOW"):
        print (Fodd)
    elif command == ("ADD"):
        Food = input("Please enter the thing you want: ")
        if Food == (" "):
            print("Are you really want to save spacebar? ok.")
            Fodd.append(Food)
        elif len(Food) == 0:
            print("Memory for the nothing is infinite. I don't want to do it that long.")
        else:
            print("New thing added!")
            Fodd.append(Food)
    elif command == ("END"):
        print ("Ok im going to shop... wait... I don't have legs.")
        listing = False
    else:
        print("What does that mean?")
