def clear_none(my_list):
    last_valid_value = None
    for i in range(len(my_list)):
        if my_list[i] is None:
            my_list[i] = last_valid_value
        else:
            last_valid_value = my_list[i]
    return my_list


my_list = [3, 5, 2, False, 8, None, 5, False, None]
print(clear_none(my_list))