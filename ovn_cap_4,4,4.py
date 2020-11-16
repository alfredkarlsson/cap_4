                     ####### Alfred Karlsson #########

number_of_rows = int(input("How many rows do you want?"))
position = 1
startnumber = 1
multiplier = 1



for x in range(1, number_of_rows + 1):
    if number_of_rows >= x:
        while number_of_rows >= position:
            thing = startnumber * multiplier
            if thing >= 1000 and thing < 10000000000:
                print(f"{thing} ", end = "")
            if thing >= 100 and thing < 1000:
                print(f"{thing}  ", end = "")
            if thing >= 10 and thing < 100:
                print(f"{thing}   ", end = "")
            if thing < 10:
                print(f"{thing}    ", end = "")
            if thing >= 10000000000:
                print("NUMBER IS TOO BIG")
                break
            multiplier += 1
            position += 1
        else:
            print("\n")
            startnumber += 1
            multiplier = 1
            position = 1