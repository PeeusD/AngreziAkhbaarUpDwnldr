import requests
from PyDictionary import PyDictionary

def word_searching(get_string): 
    
    english_most_common_10k = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa-no-swears.txt'

    # Get the file of 10 k most common words from TXT file in a github repo
    response = requests.get(english_most_common_10k)
    data = response.text

    set_of_common_words = {x for x in data.split('\n')}

    # Once we have the set of common words, we can just check.
    # The check is in average case O(1) operation,
    # but you can use for example some sort of search three with O(log(n)) complexity

    
        
    new_string = get_string.lower()
    punc = '''!()=-[]{};:—'"\,<>./?@#$%^&*_~1234567890'''

    for ele in new_string:
        if ele in punc:
            new_string = new_string.replace(ele, "")
    words = new_string.split()
    
    dict_obj = PyDictionary()
    # searching required word-meaning in PyDict
    wrd_mng = {}
    for word in words:    
        if word in set_of_common_words:
            pass
        else:
            meaning = dict_obj.meaning(word, disable_errors=True)
            if meaning is not None:
                # appending word and meanings into dict
                wrd_mng[word] = meaning
    
    return wrd_mng
    # word_searching('deploy deprecated')      