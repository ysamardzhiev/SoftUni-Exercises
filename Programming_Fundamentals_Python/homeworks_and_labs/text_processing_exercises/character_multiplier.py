string1, string2 = input().split()

largest_string = max(len(string1), len(string2))
smallest_string = min(len(string1), len(string2))

total_sum = 0
for i in range(largest_string):
    if i < smallest_string:
        total_sum += ord(string1[i]) * ord(string2[i])
    else:
        if len(string1) == largest_string:
            largest_string = string1
        else:
            largest_string = string2
        total_sum += ord(largest_string[i])
print(total_sum)