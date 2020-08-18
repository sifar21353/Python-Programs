input_str = input('Enter str: ')
word = ''
final = ''

def length(string):
  count = -1
  for i in string:
    count += 1
  return count

def reverse(string):
  count = length(string)
  a = ''
  for i in range(count + 1):
    a += string[count]
    count -= 1
  return a

count = length(input_str)

for i in range(count + 1, 0, -1):

  if input_str[i - 1] == ' ':
    word = reverse(word) + ' '
    final += word
    word = ''
  else:
    word += input_str[count]

  count -= 1

word = reverse(word) + ' '
final += word
print(final)
