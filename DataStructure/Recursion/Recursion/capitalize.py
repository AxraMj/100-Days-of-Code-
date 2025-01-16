word="Hello world"

def capitalize():
    result=[i.upper() for i in word.split()]
    return result

print(capitalize())

#now using recursion

sentence="My Name is Akshara Manoj"
sentence_split=sentence.split()
def capitalize_word(sentence_split,index=0):
    if index==len(sentence_split):
        return []
    return [sentence_split[index].upper()] + capitalize_word(sentence_split,index+1)

print(capitalize_word(sentence_split))
