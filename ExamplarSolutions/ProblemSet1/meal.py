def main():
    answer = input("What's the fookin toime bruv: ")
    meal = convert(answer)
    if meal != "WOMP WOMP NO FOOD FOR YOU UGLY":
        print(meal)


def convert(time): 
    hours, minutes = time.split(":", 1)
    hours = int(hours)
    minutes = int(minutes)
    if hours == 7 or (hours == 8 and minutes == 0):
        return "breakfast time"
    elif hours == 12 or (hours == 13 and minutes == 0):
        return "lunch time"
    elif hours == 18 or (hours == 19 and minutes == 0):
        return "dinner time"
    else:
        return "WOMP WOMP NO FOOD FOR YOU UGLY"

if __name__ == "__main__":
    main()