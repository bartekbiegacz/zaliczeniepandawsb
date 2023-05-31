#zaimportowanie danych z excela

import pandas as pd
pd.read_excel(r'C:\Users\vdi-student\Desktop\zaliczenie panda\danezaliczenie.xlsx')

#utworzenie pustego DataFrame

import pandas as pd
zbior = pd.DataFrame()
print(zbior)

#dataframe poprzez liste

lista = [2,3,4,5]
print(pd.DataFrame(lista))

#dateframe poprzez slownik

slownik = {'Imie':['bartosz','kamil','iza'], 'Wiek':[27,43,36]}
print ( pd.DataFrame(slownik))