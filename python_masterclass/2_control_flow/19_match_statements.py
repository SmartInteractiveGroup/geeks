#match case statements --> upper 3.10
belt_color = input("Insert your ninja color:")

match belt_color:
    case "white":
        print("Newby")
    case "red":
        print("Intermadiate")
    case "black":
        print("Master")
    case _:                       #default
        print("omg")