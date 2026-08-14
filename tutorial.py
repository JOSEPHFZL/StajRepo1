import pandas as pd

# Dosyadan veriyi oku
data = pd.read_csv('joseph.csv')

# print(data)

# Verileri baştan göster ( istenen sayı kadar gösterebilir )
# print(data.head(1))

# Verileri sondan göster ( istenen sayı kadar gösterebilir )
# print(data.tail(2))

# Kaç adet veri var ?
# print(data.shape)

# Veri hakkında bilgi edinelim
# print(data.info())

# Belirli bir sütuna ait verileri getir
# print(data['Ad'])
# print(data[['Ad','Yas']])

# Belirli bir sutuna ait verileri index numaraları ile getir ( Integer location )
# print(data.iloc[0:])
# print(data.iloc[1,0])
# print(data.iloc[[1,2],0])
# print(data.iloc[1,[0,1]])
# print(data.iloc[[1,2],[0,1]])

# Belirli bir sutuna ait verileri index numaraları ile getir ( Label location )
# print(data.loc[[0,1]])
# print(data.loc[[0,1], "Ad"])
# print(data.loc[[0,1], ["Ad", "Yas"]])
# print(data.loc[0:2])

# Örnek filtrelemeler ( bir sonraki sessionda daha detaylı bakılacak )

# print(data.loc[data["Yas"] == 21])
print(data.loc[data["DogumYeri"] == 'İSKENDERUN'])