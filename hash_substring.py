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
    i = 0
    j = 0
    d = 256
    prime = 1000000
    p = 0 # hash vertiba petternam
    t = 0 # hash vertiba stringam
    h = 1
    occurances = []

    for i in range(p_len-1):
        h = (h * d) % prime
    
    for i in range(p_len):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    for i in range(t_len - p_len + 1):
        if p==t:
            for j in range(p_len):
                if text[i+j] != pattern[j]:
                    break
            j+=1
            if j == p_len:
                occurances.append(i)
        if i < t_len - p_len:
            t = (d*(t-ord(text[i])*h) + ord(text[i+p_len])) % prime

            if t<0:
                t = t + prime
    return occurances




    # and return an iterable variable
    

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

