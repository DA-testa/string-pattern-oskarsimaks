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
    p = len(pattern)
    t = len(text)
    result = []
    prime = 1000000007
    x = 1
    p_hash = 0
    t_hash = 0
    for i in range(p):
        p_hash = (p_hash + ord(pattern[i]) * x) % prime
        t_hash = (t_hash + ord(text[i]) * x) % prime
        x = (x * 263) % prime

    for i in range(t - p + 1):
        if p_hash == t_hash and text[i:i+p] == pattern:
            result.append(i)
            
        if i < t - p:
            t_hash = (t_hash - ord(text[i]) * x) % prime
            t_hash = (t_hash * 263 + ord(text[i+p])) % prime

    # and return an iterable variable
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

