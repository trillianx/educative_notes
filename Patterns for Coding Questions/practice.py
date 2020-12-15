def longest_substrings_with_k_distinct(string, k):
    start = 0
    max_length = 0
    substring = ''
    for end in range(len(string)):
        substring += string[end]
        unique_chars = len(set(substring))
        while unique_chars > k:
            cur_length = end - start + 1
            max_length = max(max_length, cur_length)
            substring = substring[start:]
            start += 1
            unique_chars = unique_chars - 1
            # print(substring)
    return max_length - 1

if __name__ == "__main__":
    string = 'araaci'
    k = 1
    print(longest_substrings_with_k_distinct(string, k))