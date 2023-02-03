input_sent = []
result = []

def recursion(s, l, r):
    if l >= r:
        return 1, l+1
    elif s[l] != s[r]:
        return 0, l+1
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

def user_input(repeat_time):
    for _ in range(repeat_time):
        u_input = input()
        input_sent.append(u_input)

def check_time_inPalindrome(repeat_time):
    for i in range(repeat_time):
        result.append(isPalindrome(input_sent[i]))
    for i in range(repeat_time):
        print(result[i][0], result[i][1])

repeat_time = int(input())
user_input(repeat_time)
check_time_inPalindrome(repeat_time)