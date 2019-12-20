'''
question number 4
'''
def generate_3d_array(l):
    last_list = []
    for loop_count in range(0,l):
        last_list.append([0 for i in range(0,3)])
    return last_list


print(generate_3d_array(8))