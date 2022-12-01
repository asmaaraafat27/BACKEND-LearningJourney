def reverse_string(string_s):
    if(len(string_s)) == 0:
        return string_s
    else:
        return reverse_string(string_s[1:])+string_s[0]

print(reverse_string("reversal"))
