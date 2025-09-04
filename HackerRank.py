##################### 1
# n = int(input())
string = ''
n = 15
if 1 <= n <= 150:
    for i in range(1, n + 1):
        string += str(i)
print(string)


################## 2
def swap_case(s):
    if 0 < len(s) <= 1000:
        return s.swapcase()
    else:
        return None


################## 3
def split_and_join(line):
    spl = line.split(" ")
    return "-".join(spl)


# or -> Replace all spaces with -

################## 4
def mutate_string(word, position, character):
    return word[:position] + character + word[position + 1:]

################## 5
def count_substring(word, sub_string):
    count = 0
    if 1 <= len(word) <= 200:
        for i in range(len(word) - len(sub_string) + 1):
            if word[i:i+len(sub_string)] == sub_string:
                count += 1
    return count
