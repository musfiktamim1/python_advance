day = 2
month = 2

match day:
    case 1:
        print("yes")
    case 2:
        print("no")
    case _:
        print("not found")

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("this is week day")
    case 6|7:
        print("this is weekends")
    case _:
        print("invalid input")

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 1:
        print("A weekday in January")
    case 1 | 2 | 3 | 4 | 5 if month == 2:
        print("A weekday in Fabruary")
    case _:
        print("no match")
