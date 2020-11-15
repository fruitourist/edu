def huffman_algorithm(text: str) -> tuple:

    count_char = dict()
    for char in text:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    
    leaf = sorted(counter_char.items(), key = lambda char: char[1])
    
    #processing

    #test
    return (counter_char, leaf)


#test
output = huffman_algorithm("воровал варвар у варвара варево")
print(output)
