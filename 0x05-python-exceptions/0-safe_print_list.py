def safe_print_list(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end=" ")
        except (IndexError, TypeError):
            break
        else:
            counter += 1
    print()
    return counter

