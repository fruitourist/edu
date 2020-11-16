from heapq import heappush, heappop, heapify
from collections import defaultdict


def huffman_algorithm(text: str) -> list:

    count_char = defaultdict(int)
    for char in text:
        count_char[char] += 1
    
    heap = [[wt, [char, str()]] for char, wt in count_char.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap) #
        hi = heappop(heap) #

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]

        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heappop(heap)[1:], key = lambda pair: (len(pair[-1]), pair))


#test
output = huffman_algorithm("четыре черненьких чумазеньких чертенка чертили черными чернилами чертеж")
print(output)
