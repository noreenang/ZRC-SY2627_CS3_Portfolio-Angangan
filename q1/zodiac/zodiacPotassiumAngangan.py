# Activity 3: Chinese Zodiac Sign
# Name: Noreen Ysabelle C. Angangan

try:
    year = int(input("Enter your birth year: "))

    if year < 1900:
        print("Invalid year. It should not be earlier than 1900.")
    else:
        zodiac_index = (year - 1900) % 12

        if zodiac_index == 0:
            print("Your Chinese Zodiac Sign is: Rat (鼠/Shū)")
        elif zodiac_index == 1:
            print("Your Chinese Zodiac Sign is: Ox (牛/Niú)")
        elif zodiac_index == 2:
            print("Your Chinese Zodiac Sign is: Tiger (虎/Hú)")
        elif zodiac_index == 3:
            print("Your Chinese Zodiac Sign is: Rabbit (兔/Tù)")
        elif zodiac_index == 4:
            print("Your Chinese Zodiac Sign is: Dragon (龙/ Lóng)")
        elif zodiac_index == 5:
            print("Your Chinese Zodiac Sign is: Snake (蛇/Shé)")
        elif zodiac_index == 6:
            print("Your Chinese Zodiac Sign is: Horse (马/Mǎ)")
        elif zodiac_index == 7:
            print("Your Chinese Zodiac Sign is: Goat (羊/ Yáng)")
        elif zodiac_index == 8:
            print("Your Chinese Zodiac Sign is: Monkey (猴/Hóu)")
        elif zodiac_index == 9:
            print("Your Chinese Zodiac Sign is: Rooster (鸡/Jī)")
        elif zodiac_index == 10:
            print("Your Chinese Zodiac Sign is: Dog (狗/Gǒu)")
        elif zodiac_index == 11:
            print("Your Chinese Zodiac Sign is: Pig (豬/Zhū)")

except ValueError:
    # Checking for non-number inputs (like letters or symbols)
    print("Invalid Input! Please enter a valid numerical year.")

