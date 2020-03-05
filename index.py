with  open('currency_converter.txt') as cr:
    lines=cr.readlines()
cdict = {}
for line in lines:
    con = line.split('\t')
    cdict[con[0]] = con[1]

amount=int(input('Enter any one of the country name listed here : '))
[print(item) for item in cdict.keys()]
crr= input('enter the values: ')
print(f' {amount} inr to equal to {amount * float(cdict[crr])} {crr}')
