def fact(num):
    result = 1
    if num > 0:
        result = num * fact(num-1)
    return result

user_input = int(input())
print(fact(user_input))