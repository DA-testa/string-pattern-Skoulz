# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    

    users_input = input()

    if "I" in users_input:
        pattern=input().rstrip()
        text=input().rstrip()
        return (pattern, text)

    elif "F" in users_input:
        with open(str("./tests/06"), mode="r", encoding='UTF-8') as files:
            pattern = files.readline()
            text = files.readline()
        return (pattern.rstrip(), text.rstrip())
    else:
        print("Input error")
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    return pattern, text

    # this is the sample return, notice the rstrip function
   # return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    pattern_length, text_length = len(pattern), len(text)
    users_hash_1 = hash(pattern)
    users_hash_2 = hash(text[:pattern_length])
    occurrences = []
    for i in range(text_length - pattern_length + 1):
        if users_hash_1 == users_hash_2 and pattern == text[i:i+pattern_length]:
            occurrences.append(i)
        if i < text_length - pattern_length:
            users_hash_2 = (users_hash_2 - ord(text[i]) * pow(10, pattern_length-1)) * 10 + ord(text[i+pattern_length])
    return occurrences
    
    # and return an iterable variable
   #return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

