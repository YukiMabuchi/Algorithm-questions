num_list = input('Please enter a list of numbers separated by space : ' ).split()

temp_list = []

def perm(start, end=[]):

    if(len(start) == 0):
        temp_list.append(end)
    else:
        for i in range(len(start)):
            perm(start[:i] + start[i+1:], end + start[i:i+1])

    permutations_list = list({int(''.join(map(str, v))) for v in temp_list})

    return permutations_list
            
permutations = perm(num_list)
print(f'All permutations of {num_list} are {sorted(permutations)}')
