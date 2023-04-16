# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    decis = input()
    # Nolasit no klavieturas
    if "I" in decis:
        pattern = input().rstrip()
        text = input().rstrip()
    # Nolasit no faila
    elif "F" in decis:
        file= input()
        if "a" in file:
            return
        with open(f"./tests/{file}", mode="r") as file:
            pattern = int(file.readline())
            text = list(map(int, file.readline().split(" ")))
    else:
        return

    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p_len = len(pattern)
    t_len = len(text)

    p_hash = hash.string(pattern)
    t_hash = None
    occurrences = []

    for i in range(t_len - p_len + 1):
        # calculate hash of current substring of text if it has not been calculated already
        if t_hash is None:
            t_hash = hash_string(text[i:i+p_len])
        # if hashes match, check if pattern and substring are equal
        if p_hash == t_hash:
            if pattern == text[i:i+p_len]:
                occurrences.append(i)
        # if hashes don't match, calculate hash of next substring of text
        if i < t_len - p_len:
            t_hash = recalculate_hash(text[i:i+p_len], text[i+p_len], t_hash)

    

    # and return an iterable variable
    return occurrences

def hash_string(string):
    hash_val = 0
    for char in reversed(string):
        hash_val = (hash_val * 263 + ord(char)) % (10**9 + 7)
    return hash_val


def recalculate_hash(substring, next_char, old_hash):

    old_char = substring[0]
    new_hash = (old_hash - ord(old_char) * 263**(len(substring)-1)) * 263 + ord(next_char)
    return new_hash % (10**9 + 7)

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

