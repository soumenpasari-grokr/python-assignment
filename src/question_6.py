def get_special_nums(enum_var):
    for curr_number in range(0,enum_var):
        # checking for number 5
        if(curr_number != 0):
            if(curr_number % 5 == 0):
                yield curr_number
            elif(curr_number % 7 == 0):
                yield curr_number

last_range = int(input('Enter the range : \n'))

for value in get_special_nums(last_range):
    print(value,end=',')


