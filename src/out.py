
def convert_input(user_input):
    try:
        return int(user_input)
    except ValueError:
        try:
            return float(user_input)
        except ValueError:
            return user_input
if __name__ == '__main__':
    s = None
    s= input()
    s = convert_input(s)
    ans=True
    len = len(s)
    i = 0
    for i in range(int(i), int(len/2)):
        if s[i]!=s[len-1-i]:
            ans=False
    if ans:
        print("True" + "\n")
    else:
        print("False" + "\n")
