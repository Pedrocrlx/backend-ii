# def linear_search(lst, target):
#     for item in lst:
#         if item == target:
#             return True
#     return False

## print(linear_search([4,10,5], 10))

## Exercise -----------------------

# count = 0

# def recursive(n):
#     if n == 1:
#         return 1
#     else:
#         global count 
#         count += 1
#         return n * recursive(n - 1)

# print(recursive(10))
# print(f"The function was called {count} times")

## ---------------------------

## challenge
numbers_challenge = [1, 6, 8, 4, 2, 9, 7, 10, 3, 5, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
challenge_count = 0

def binary_search(array):
    global challenge_count
    challenge_count += 1
    array.sort()
    mid = (array[0] + array[-1]) // 2
    return print(f"Mid: {mid}, Count: {challenge_count}")

binary_search(numbers_challenge)

                
