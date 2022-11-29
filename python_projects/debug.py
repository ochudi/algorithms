# Merge Sort

def merge_sort(my_list):
    if (len(my_list) > 1):
        middle_index = len(my_list) // 2
        left_list = my_list[:middle_index]
        right_list = my_list[middle_index:]

        merge_sort(left_list)
        merge_sort(right_list)

        left_index = 0
        right_index = 0
        current_index = 0

        while (left_index < len(left_list) and right_index < len(right_list)):
            if (left_list[left_index] < right_list[right_index]):
                my_list[current_index] = left_list[left_index]
                left_index += 1
                current_index += 1
            else:
                my_list[current_index] = right_list[right_index]
                right_index += 1
                current_index += 1

        while (left_index < len(left_list)):
            my_list[current_index] = left_list[left_index]
            left_index += 1
            current_index += 1

        while (right_index < len(right_list)):
            my_list[current_index] = right_list[right_index]
            right_index += 1
            current_index += 1


random_list = [20, 4, 5, 40, 10]
merge_sort(random_list)
print(random_list)