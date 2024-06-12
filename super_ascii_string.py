def check_super_ascii(s):
    list1 = [0]*26
    for i in s:
        list1[ord(i)-97] +=1
    for i in s:
        if list1[ord(i)-97] != ord(i)-96:
            return False
    return True

string1 = input("Enter any string: ")
if check_super_ascii(string1):
    print("It is a super ascii string.")
else:
    print("It is not a super ascii string.")
