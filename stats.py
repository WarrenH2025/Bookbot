def get_num_words(text):
    text_split= text.split()
    return len(text_split)

def get_char_count(text):
    text = list(text)
    char_dict = {}
    
    for i in text:
        if i.isalpha():
            if i not in char_dict:
                char_dict[i] = 1
            else:
                char_dict[i] += 1
    sorted_dict = sorted(char_dict.items(), key= lambda item : item[1], reverse = True)
    
    return sorted_dict
    


        


    
