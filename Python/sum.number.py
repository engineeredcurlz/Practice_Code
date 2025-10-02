## sum numbers in a list

def sum_list(nums):
    total_sum = 0
    for num in nums:
        total_sum += num
    return total_sum

list = [1, 2, 3]
result = sum_list(list)
print(f"The sum of the list is: {result}")