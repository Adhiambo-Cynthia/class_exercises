squares = []
for i in range(10):
  squares.append(i * i)
print(squares)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
'''
Rather than creating an empty list and adding each element to the end, you simply define the list 
and its contents at the same time by following this format:
new_list = [expression, for member in iterable]
'''
squares = [i * i for i in range(10)]
print(squares)
'''
Because the expression requirement is so flexible,
 a list comprehension in Python works well in many places where you would use map()
'''
txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)
final_prices = [get_price_with_tax(i) for i in txns]
print(list(final_prices))
#if it was map
#final_prices=map(get_price_with_tax, txns)
'''Conditionals are important because they allow list comprehensions to filter out unwanted values,
 which would normally require a call to filter():'''
sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']
print(vowels)
#['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']
sentence = 'The rocket, who was named Ted, came back from Mars because he missed his friends.'
vowels= "a e i o u"
consonants = [i for i in sentence if i not in vowels]
print(consonants)