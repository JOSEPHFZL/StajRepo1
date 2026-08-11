import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from numpy import nan as NA


# obje=pd.Series(["ali",23,"muhendis"])
# print(obje)

veri={"Isim":["ahmet","ali","mehmet","selin","gamze","pelin"],
      "Puan":[87,98,90,56,43,78],
      "Spor":["Güres","futbol","basketbol","bale","tennis","voleybol"],
      "Cinsiyet":["E","E","E","K","K","K"]}

df=pd.DataFrame(veri)
# print(df)
# print(df.head()) ilk 5 veriyi gösterir.
# print(df.head(2)) ilk 2 veriyi gösterir.
# print(df.tail()) son 5 veriyi gösterir.
# print(df.tail(3)) son 3 veriyi gösterir.

df=pd.DataFrame(veri,columns=["Isim","Spor","Cinsiyet","Puan","Yas"],
                index=[5,4,3,2,1,0]) 
# print(df) yas olmayan bir degisken oldugu icin eklenir ama degerler NaN olarak gözukur.
# print(df) indexi istedegimiz sekılde yazabılırız

sutunlarim=["Isim","Spor"] #degisken kullanma sebebimiz df komutu sadece bi tane index alır.
# print(df[sutunlarim])
# print(df.loc[[4]]) 
df["Yas"]=18
# print(df)
df["Yas"]=[15,23,42,12,15,18]
# print(df)
df["Gecti"]=df.Puan>70
# print(df)
del df["Gecti"]
# print(df) sildi

notlar={"Mat":{"Ali":85,"Efe":90,"Nur":95},
        "Fiz":{"Ali":90,"Efe":80,"Nur":75}}
puan=pd.DataFrame(notlar)
# print(puan)
# print(puan.T) tersini alıyor 

# indeks=puan.index #bu komuttan sonra herhangi bi index degisimi yapamazsın.
# indeks[1]="can"
# print(indeks)

obje=pd.Series(np.arange(5),index=["a","b","c","d","e"])

# print(obje)

veri=pd.DataFrame(np.arange(16).reshape(4,4),index=["Bursa","Ankara","Rize","Istanbul"],
                  columns=["bir","iki","uc","dort"])

# print(veri)
# print(veri[["bir","iki"]]) #iki tane köseli parantez kullanma sebebimiz 1 den fazla index yazıyor olmamızdır.

# print(veri.iloc[1])
# print(veri.iloc[1,[1,2,3]]) 0. indexi almadık.

veri=pd.Series(np.arange(5),index=["a","b","c","d","e"])

# print(veri)
# print(veri.iloc[-1]) son elamnı aldı

s=pd.Series(["ege",np.nan,"ali","eda"])
# print(s)
# print(s.isnull())
s[3]=None
# print(s.dropna()) #eksik verileri kaldırır

df=pd.DataFrame([[1,2,3],[4,NA,5],[NA,NA,NA]])
# print(df)
# print(df.dropna())
# print(df.dropna(how="all")) #butun degerleri eksik olanı gösterir.
df[1]=NA 
# print(df)
# print(df.dropna(axis=1,how="all")) #axis=1 sutun icin

# print(df.dropna(thresh=1)) #en az bi deger bulunan satir yazdırdı 
# print(df.fillna(0)) #nan degerleri yerine 0 gelir.

# print(df.fillna({0:15,1:25,2:35})) #eksik verilerin yerine (sutun olarak bakar) girilen sayıları yazar 
# df.fillna(0,inplace=True) nan olanlar 0 olur
# print(df)

df=pd.DataFrame([[1,2,3],[4,NA,5],[NA,NA,NA]])
# print(df)
# print(df.ffill()) #her bos gordugu degeri bi ustundeki degerle esitler.
# print(df.ffill(limit=1)) #her bos gordugu degeri bi ustundeki degerle esitler.(sadece 1 yapar limit=1 iken)

veri=pd.Series([1,0,NA,5])
# print(veri)

# print(veri.fillna(veri.mean())) #eksik veri yerine ortalamayı yazdıran komut

# print(df.fillna(df.mean())) #DataFrame de eksik veriler yerine ortalamayı yazdıran komut  

veri=pd.DataFrame({"a":["bir","iki"]*3,"b":[1,1,2,3,2,3]})
# print(veri)

#print(veri.duplicated()) #satır tekrarının dogrulugunu gösterir.
#print(veri.drop_duplicates()) #tekrar eden satırları kaldırır.



