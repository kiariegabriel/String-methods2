from string import punctuation
s=input('Enter the numbers:\n')
for c in punctuation:
	s=s.replace(c,'')
l=[]
for i in s:
	l.append(i)
print(l)
n_s='+'.join(l)
print(n_s)