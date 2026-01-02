def two_sum(nums, target) -> list[int]:
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [i, num_to_index[complement]]
        num_to_index[num] = i
    return []
