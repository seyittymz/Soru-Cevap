def replace_word(words):
    punc_str = '!,.?:;'
    for i in words:
        if i in punc_str:
            words = words.replace(i,"")
    return words


def avg_len(text):
    text  = replace_word(text)
    word_list = text.split(' ')
    print(word_list)
    total_length = 0
    for word in word_list:
        total_length += len(word)
    
    final = (total_length/len(word_list))
    
    return final
    

                
        
    
    
    
print(avg_len('Elma, Armut, Portakal'))