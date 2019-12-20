a = [1,2,3,5,6]
b = [num*num for num in a]
print(b)

name = "Kushagra"
chars = [char.upper() for char in name]
print(chars)

numbers = list(range(1,30))

even = [num for num in numbers if num%2==0]
odd = [num for num in numbers if num%2 !=0]

print(even)
print(odd )

[num*2 if num%2 ==0  else num/3 for num in numbers]

sent = "A quick brown fox jumps over the lazy dog."

w_vowels = [char for char in sent if char not in 'aeiou']
print(w_vowels)
''.join(w_vowels)
len(w_vowels)

f_name = "Kushagra"
l_name = "Kumar"

' '.join([f_name, l_name])
