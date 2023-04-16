#221RDB060 Artjoms Sidorkins
# python3

def read_input():
    # this function needs to acquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow

    users_input = input()

    if "I" in users_input:
        pattern=input().rstrip()
        text=input().rstrip()


    if "F" in users_input:
        with open(str("tests/06"), mode="r", encoding='UTF-8') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    return (pattern, text)
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    #return pattern, text

    # this is the sample return, notice the rstrip function
   # return (pattern, text)
def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin Karp algorithm
    pattern_length, text_length = len(pattern), len(text)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:pattern_length])
    occurrences = []
    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash and pattern == text[i:i+pattern_length]:
            occurrences.append(i)
        if i < text_length - pattern_length:
            text_hash = (text_hash - ord(text[i]) * pow(10, pattern_length-1)) * 10 + ord(text[i+pattern_length])
    return occurrences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
