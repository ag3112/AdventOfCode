def concat(a, b):
    return int(str(a) + str(b))


def perform_operation(nums, ops):
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i + 1]
        elif ops[i] == '*':
            result *= nums[i + 1]
        else:
            result = concat(result, nums[i + 1])
    return result


def is_equal(target, nums):
    if len(nums) == 1:
        return target == nums[0]

    operators = ['+', '*', '||']
    n = len(nums) - 1

    for op_combo in range(3 ** n):
        ops = []
        curr = op_combo
        for _ in range(n):
            ops.append(operators[curr % 3])
            curr //= 3

        if perform_operation(nums, ops) == target:
            return True

    return False


total = 0
with open('data.txt', 'r') as file:
    for line in file:
        target, nums = line.split(': ')
        target = int(target)
        nums = [int(x) for x in nums.split()]

        if is_equal(target, nums):
            total += target
print(total)
