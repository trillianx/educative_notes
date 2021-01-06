def count_string(string, character, count):
    if len(string) == 0:
        return count
    else:
        if string[0] == character:
            return count_string(string[1:], character, count+1)
        else:
            return count_string(string[1:], character, count)


if __name__ == "__main__":
    string = "abacada"
    result = count_string(string, 'a', 0)
