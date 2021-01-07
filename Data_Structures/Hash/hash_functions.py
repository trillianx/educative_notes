def hash_modular(key, size):
    return key % size

def hash_truncate(key):
    return key % 1000  # this gives us a key of up to 3 digits

def hash_fold(key, chunk_size):
    str_key = str(key)  # Convert integer into string for slicing
    print("Key: " + str_key)
    hash_val = 0
    print("Chunks:")
    for i in range(0, len(str_key),  chunk_size):

        if(i + chunk_size < len(str_key)):
            # Slice the appropriate chunk from the string
            print(str_key[i:i+chunk_size])
            hash_val += int(str_key[i:i+chunk_size])  # convert into integer
        else:
            print(str_key[i:len(str_key)])
            hash_val += int(str_key[i:len(str_key)])
    return hash_val


if __name__ == "__main__":
    key = 3456789
    chunk_size = 2
    print(hash_fold(key, chunk_size))