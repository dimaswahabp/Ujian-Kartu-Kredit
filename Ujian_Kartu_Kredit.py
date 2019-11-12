import json

with open('ccNasabah.json','r') as x:
    out = json.load(x)

letter = ['a','b','c','d','e','f','g','h','i',
        'j','k','l','m','n','o','p','q','r','s','t','u',
        'v','w','x','y','z'
]
valid = []
invalid = []
for i in range(len(out)):
    nomor = out[i]['noCreditCard']
    nomor = nomor.split('-')
    nomor = ''.join(nomor)
    # print(nomor[0])
    if nomor[0]=='4' and len(nomor) == 16:
        # for j in range(len(nomor)):
        #     if nomor[j].isalpha():
        #         invalid.append(out[i])
            
        if ' ' in nomor:
            invalid.append(out[i])
        elif nomor[i].isalpha():
            invalid.append(out[i])
        elif '-' in nomor:
            invalid.append(out[i])
        elif '44444' in nomor:
            invalid.append(out[i])
        else: 
            valid.append(out[i])
    elif nomor[0] == '5' and len(nomor) == 16:
        # for j in range(len(nomor)):
        #     if nomor[j].isalpha():
        #         invalid.append(out[i])
        
        if ' ' in nomor:
            invalid.append(out[i])
        elif nomor[i].isalpha():
            invalid.append(out[i])
        elif '-' in nomor:
            invalid.append(out[i])
        elif '9999' in nomor:
            invalid.append(out[i])
        else:
            valid.append(out[i])
    elif nomor[0] == '6' and len(nomor) == 16:
        # for j in range(len(nomor)):
        #     if nomor[j].isalpha():
        #         invalid.append(out[i])
        if ' ' in nomor:
            invalid.append(out[i])
        elif nomor[i].isalpha():
            invalid.append(out[i])
        elif '-' in nomor:
            invalid.append(out[i])
        elif '61234' in nomor:
            invalid.append(out[i])
        else: 
            valid.append(out[i])
    else:
        invalid.append(out[i])

with open('ccValid.json','w') as y:
    json.dump(valid,y)
with open('ccInvalid.json','w') as yy:
    json.dump(invalid,yy)