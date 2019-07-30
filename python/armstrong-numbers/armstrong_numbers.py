def is_armstrong_number(number):
    number_ls = list(str(number))
    result = 0

    for i in number_ls:
        result += int(i)**len(number_ls)

    if result == number:
        return True
    else:
        return False
