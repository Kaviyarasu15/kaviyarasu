a=raw_input()
if len(a)<100000:
b=['d','h','o','n','i']
l=[]
for i in range(0,len(a)):
l.append(a[i])
res=[]
if len(l)==len(b):
for i in l:
if i in b:
if i not in res:
res.append(i)
if len(res)==len(b):
print "yes"
else:
print "no"
else:
print "no"
else:
print "Invalid"
