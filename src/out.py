
def convert_input(user_input):
    try:
        return int(user_input)
    except ValueError:
        try:
            return float(user_input)
        except ValueError:
            return user_input
def isPalindrome(s: str) -> bool:
    str_len = len(s)
    i = 0
    for i in range(int(i), int(str_len/2)):
        if s[i]!=s[str_len-1-i]:
            return False
    return True
if __name__ == '__main__':
    s = None
    s= input()
    s = convert_input(s)
    ans=isPalindrome(s)
    if ans:
        print("True" + "\n")
    else:
        print("False" + "\n")
