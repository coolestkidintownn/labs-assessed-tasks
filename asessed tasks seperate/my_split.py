def my_split(my_str, sep):
    temp_str = ""
    split_strs = []

    for i in my_str:
        temp_str = temp_str + i
        if i == sep:
            split_strs.append(temp_str[:-1])
            temp_str = ""
    split_strs.append(temp_str)

    return split_strs

print(my_split("apple,banana,orange", ","))
