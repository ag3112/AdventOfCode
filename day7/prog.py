def perform_operation(nums, ops):
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i + 1]
        else:
            result *= nums[i + 1]
    return result


def is_equal(target, nums):
    if len(nums) == 1:
        return target == nums[0]

    def try_this(pos, curr_ops):
        if pos == len(nums) - 1:
            return perform_operation(nums, curr_ops) == target

        return (try_this(pos + 1, curr_ops + ['+']) or
                try_this(pos + 1, curr_ops + ['*']))

    return try_this(0, [])


total = 0
with open('data.txt', 'r') as file:
    for line in file:
        target, nums = line.split(': ')
        target = int(target)
        nums = [int(x) for x in nums.split()]

        if is_equal(target, nums):
            total += target
print(total)
