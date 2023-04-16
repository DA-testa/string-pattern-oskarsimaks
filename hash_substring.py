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
    p = 10**9 + 7  
    x = 263 
    result = []
    pattern_hash = sum([ord(pattern[i])*pow(x, i, p) for i in range(len(pattern))]) % p
    text_hash = sum([ord(text[i])*pow(x, i, p) for i in range(len(pattern))]) % p
    x_to_n = pow(x, len(pattern), p)
    
    for i in range(len(text)-len(pattern)+1):
        if pattern_hash == text_hash and pattern == text[i:i+len(pattern)]:
            result.append(i)
        if i < len(text)-len(pattern):
            text_hash = (text_hash - ord(text[i])*x_to_n) % p
            text_hash = (text_hash*x + ord(text[i+len(pattern)])) % p
            text_hash = (text_hash + p) % p
    # and return an iterable variable
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

