from itertools import product

def solution(word):
    
    answer = 0
    word_list = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    for i in range(1,len(word_list)+1):
        for c in product(word_list, repeat = i):
            words.append("".join(c))
            
            
    words.sort()
    
    return words.index(word) + 1
    