#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    return [safe_division(my_list_1[i], my_list_2[i]) for i in range(list_length)]

def safe_division(a, b):
    try:
        return a / b
    except (ValueError, TypeError):
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    return 0

