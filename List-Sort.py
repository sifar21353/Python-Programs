l = list(input('Please enter the numbers: '))
sort = input('Please enter way of sorting: ascending or descending (a/d): ')
count = 0
for i in l:
    if count == 2:
        print('hello')
        l[l.index(i - 1)] + l[l.index(i)]
        l.remove(i)
    elif i == ',':
        l.remove(i)
    else:
        count += 1

if sort == 'a':
  l.sort()
  print(l)
else:
  l.sort(reverse=True)
  print(l)