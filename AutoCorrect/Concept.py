# Part 1: Data Preprocessing
import re

# data file
filename = "shakespeare.txt"

#  processing the text
def process_data(filename):
    with open(filename, 'rb') as f:
        text = str(f.read())
        words = re.findall('\w+', text.lower())
    return words

# generating word-frequency dictionary
def get_count(word_l):
    word_freq = dict()
    for word in word_l:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

# generating word_probablity dictionary
def get_probs(word_freq):
    probs = dict()
    total = sum(list(word_freq.values()))
    for word,freq in word_freq.items():
        probs[word] = freq/total
    return probs

word_l = process_data(filename)
vocab = set(word_l)
probs = get_probs(get_count(word_l))

# Part 2: String Manipulation
class edit:
    def __init__(self, word):
        self.word = word
    
    def delete_letter(self):
        delete_l = [ self.word[:i]+self.word[i+1:] for i in range(len(self.word)) ]
        return delete_l
        
    def switch_letter(self):
        switch_l = [ self.word[:i]+self.word[i+1]+self.word[i]+self.word[i+2:] for i in range(len(self.word)-1)]
        return switch_l
        
    def replace_letter(self):
        letters = "abcdefghijklmnopqrstuvwxyz"
        replace_l = [ self.word[:i]+char+self.word[i+1:] for char in letters for i in range(len(self.word))]
        replace_set = set([w for w in replace_l if w!=self.word])
        replace_l = sorted(list(replace_set))
        return replace_l
    
    def insert_letter(self):
        letters = "abcdefghijklmnopqrstuvwxyz"
        insert_l = [ self.word[:i]+char+self.word[i:] for i in range(len(self.word)+1) for char in letters]    
        return insert_l

# Part 3: Combining edits
def edit_one_letter(word, all_switches = True):
    e = edit(word)
    edit_one_set = set(e.delete_letter() 
                       + e.switch_letter() 
                       + e.replace_letter() 
                       + e.insert_letter()
                       )
    return edit_one_set

def edit_two_letters(word):
    edit_two_set = set()
    all_words = [edit_one_letter(word) for word in edit_one_letter(word)]
    for word in all_words:
        edit_two_set = edit_two_set.union(word)
    return edit_two_set
print(len(edit_two_letters("at")))

# Part 4: Searching for the result
def get_corrections(word, probs, vocab, no_of_suggestion):
    suggestions = []
    
    if word in vocab:
        suggestions.append(word)
        
    suggestions.extend(list(edit_one_letter(word)))
    suggestions.extend(list(edit_two_letters(word)))
    
    suggestions = set([word for word in suggestions if word in vocab][:no_of_suggestion])
    best_suggestions = {word:probs.get(word, 0) for word in suggestions}
    
    best_suggestions = sorted(best_suggestions.items(), key=lambda x: x[1], reverse=True)
    
    return best_suggestions
    
suggestions = get_corrections('run', probs, vocab, 5)
print([suggestion for suggestion in suggestions])
