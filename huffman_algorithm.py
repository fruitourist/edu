def huffman_algorithm(text: str) -> dict:

    count_char = dict()
    for char in text:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    
    #processing
