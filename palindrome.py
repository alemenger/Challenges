def palindrome(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

print(palindrome("lolo"))
print(palindrome("eye"))