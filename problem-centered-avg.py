"""
PROBLEM SOLVING STEPS:
1. Understand the problem. Identify the following:
    - Inputs
    - Constraints
    - Stakeholders
    - Edge cases
2. Devise a plan
    - Confirm if we can use built-in functions or libraries
    - Think of variables
    - Pseudo code
    - Handle edge cases
    - Step by step
    - Keep it simple (brute force)
3. Implement plan
    - Determine tech stack
    - Identify data types/flow
    - Use DRY principles
4. Reflect and revise
    - Is this the most optimal solution?
    - Have all edge cases been considered?
    - Test
"""
"""
PROBLEM: centered_average (https://codingbat.com/prob/p126968)
1. Understand the problem
    - integer inputs
    - array length > 3
    - not sorted
    - has duplicates
2. Devise a plan
    - find min/max
        - sort
        - remove first and last elements
    - loop in array
        - 2 loops
        - 1 loop
    - Remove min/max values
    - Find average

"""
# Solution #1
def centered_average_v1(nums):
    min_num = min(nums)
    max_num = max(nums)
    nums.remove(min_num)
    nums.remove(max_num)
    return sum(nums) / len(nums)
    
# Solution #2
def centered_average_v2(nums):
    min_num = min(nums)
    max_num = max(nums)

    return (sum(nums) - min_num - max_num) / len(nums)
