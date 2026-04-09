## Example -----------------------

# def linear_search(lst, target):
#     for item in lst:
#         if item == target:
#             return True
#     return False

## print(linear_search([4,10,5], 10))

## Exercise -----------------------

count = 0

def recursive(n):
    if n == 1:
        return 1
    else:
        global count 
        count += 1
        return n * recursive(n - 1)

print(recursive(10))
print(f"The function was called {count} times")