
if __name__ == '__main__':

    my_list = [0, 2, 4, 8, 16, 32]

    v = next((n for n in my_list if n > 10), None)
    print("First number > 10 : " + str(v))  # 16

    v = next((n for n in my_list if n > 50), None)
    print("First number > 50 : " + str(v))  # None

    v = next((n for n in my_list if n > 50), 42)
    print("First number > 50 or 42 : " + str(v))  # 42

    v = next((n for n in my_list if n < 0), next((n for n in my_list), None))
    print("First number < 0 or First Number : " + str(v))  # 0

    v = next((n for n in my_list if n > 50), next((n for n in my_list if n > 50), None))
    print("First number > 50 or First Number > 30 " + str(v))  # 32

    v = next((n for n in my_list if n / 3 > 10), None)
    print("First number divided by 3 > 10 : " + str(v))  # 32
