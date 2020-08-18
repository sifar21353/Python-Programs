l = [11,22,33,44,55,66,78]

ln = hn = sum_list = l[0]

for i in range(1,7):
  if l[i] > hn:
    hn = l[i]
    
  elif l[i] < ln:
    ln = l[i]
  
  sum_list += l[i]

print('min ->', sum_list - hn)
print('max ->', sum_list - ln)
