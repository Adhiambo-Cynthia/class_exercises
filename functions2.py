#from functions_ import addNumbers,subtractNumbers
#addNumbers(12,45)
#from function3 import add3numbers
#add3numbers(12,56,99)


#function that reverses all the words in a sentence which contains a particular letter.
def reverse(string1,b):

    words=string1.split(' ')

    for i in words:
        if b in i:
            words2=i[::-1]
            stringb=string1.replace(i,words2)
            return stringb



print(reverse("word searches are super fun", "s"))

def reverse_begin_with(string3,x):
    words=string3.split(' ')
    for i in words:
        if i[0]==x:
            words=i[::-1]
        else:
            words=words
        return " ".join(words)

print(reverse_begin_with("word searches are super fun", "s"))

"""def double_letters(word):
    for i in range(len(word)-1):
		if word[i] == word[i+1]:
		   return True
        else:
	        return False
print(double_letters("loop"))"""

def index_of_caps(word):
  return[word.index(i) for i in word if i.isupper()]
print(index_of_caps("eDabiT"))





