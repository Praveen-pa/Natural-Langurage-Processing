strings_to_test = ["ab", "abc", "defab", "abab", "ababab","abab"]

for string in strings_to_test:
    state = 0
    for char in string:
        if state == 0 and char == 'a':
            state = 1
        elif state == 1 and char == 'b':
            state = 2
        else:
            state = 0
    if state == 2:
        print(f"'{string}' matches the pattern.")
    else:
        print(f"'{string}' does not match the pattern.")
