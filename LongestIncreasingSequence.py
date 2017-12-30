input_list = [10, 22, 9, 33, 21, 50, 41, 60, 80]
input_list1 = [10, 9, 2, 5, 3, 7, 101, 18]
input_list2 = [50, 3, 10, 7, 40, 80]
input_list1 = [10, 9, 2, 5, 3, 7, 101, 18]
input_list1 = [10, 9, 2, 5, 3, 7, 101, 18]


longest_list = {}

def find_longest_subsequence_from(index, l):
    if index >= len(l):
        return []
    else:
        sub = []
        sub.append(l[index])
        curr_index = index
        for each in l[index+1:]:
            curr_index += 1
            if each > sub[-1]:
                sub.extend(find_longest_subsequence_from(curr_index, l))
        return sub

def find_length_of_longest_increasing_subsequence(input_list):
    longest_list = {}
    for index, each in enumerate(input_list):
        if index not in longest_list:
            longest_list[index] = find_longest_subsequence_from(index, input_list)

    longest = 0
    sub = None
    for each in longest_list.values():
        if len(each) > longest:
            longest = len(each)
            sub = each
    print longest, sub

find_length_of_longest_increasing_subsequence(input_list)
find_length_of_longest_increasing_subsequence(input_list1)
find_length_of_longest_increasing_subsequence(input_list2)
#find_length_of_longest_increasing_subsequence(input_list1)
#find_length_of_longest_increasing_subsequence(input_list1)

#using Memoization
#overlapping subproblems are taken careof
#



