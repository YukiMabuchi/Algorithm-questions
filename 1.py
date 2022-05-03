from itertools import permutations

num_list = input('Please enter a list of numbers separated by space : ' ).split()

permutations_list = list(permutations(num_list))

new_l = list({int(''.join(map(str, v))) for v in permutations_list})

print(f'All permutations are {sorted(new_l)}')
