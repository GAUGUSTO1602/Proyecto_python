'''
2.2
PALÍNDROMOS
Una palabra o número palíndromo son aquellos que se leen igual de izquierda a derecha. Por ejemplo: 101 es un número palíndromo, y 236 no lo es. Ana es una palabra palíndroma y pan no lo es.
Diseña un programa que determine si un número o palabra ingresados por teclado, son palíndromos o no.
'''
print('welcome to the palindrome verify')
word = input('Please, give a word or a number\n--> ')
lower_word = word.lower()
word_reversed = len(lower_word)
result = lower_word[word_reversed::-1]
if lower_word == result:
    print(word, 'is a palindrome')
else:
    print(word, 'is not a palindrome')
    print('This is the result -->', result)