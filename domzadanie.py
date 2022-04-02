mas=['car','5','home','7','aircraft', '56','tvset','12','10','window']
masw=[]
masd=[]
for i in mas:
    if i.isalpha():
        i=str(i)
        masw.append(i)
    if i.isdigit():
        i=int(i)
        masd.append(i)
masd.sort()
maswn=sorted(masw, key=len)
print(masd)
print(maswn)
import json
with open('domzadan', 'w') as fw:
    json.dump(maswn, fw)
    json.dump(masd, fw)







