# https://evolany.larksuite.com/docs/docusHhTqzlqoBQTTTCxJW8UNac#

#inputの数字のすべての並び替えを出す
#(1, 2, 3)なら123/132/213/231/312/321
# https://www.adamsmith.haus/python/answers/how-to-generate-all-permutations-of-a-list-in-python
# https://www.monotalk.xyz/blog/python-%E6%95%B0%E5%80%A4%E6%B7%B7%E3%81%98%E3%82%8A%E3%81%AE-tuple-%E3%82%92-join-%E3%81%99%E3%82%8B/

# l = [1, 2, 39]
# new_str = ""

# for i in l:
#     changed = str(i)
#     new_str += changed


# print()

from itertools import permutations

num_list = input('Please enter a list of numbers separated by space : ' ).split()

permutations_list = list(permutations(num_list))

new_l = list({int(''.join(map(str, v))) for v in permutations_list})

print(f'All permutations are {sorted(new_l)}')


#内包表記の中身
# num_list = num.split()
# num_list = [int(v) for v in num_list]

# for i in range(len(num_list)):
#     num_list[i] = int(num_list[i])

# for i in permutations_list:
#     v = ''.join(map(str, i))
#     new_l.append(int(v))


# t = (1, 2, 4)
# print(''.join(map(str, t)))

# list_x = list(permutations(l))

# print(list_x)

# print("".join(('1', '2', '3'))) 
