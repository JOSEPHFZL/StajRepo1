def en_cok_tekrar_eden_kelime():
    # Hafta1 dosyasını oku ve veriyi icerik degiskenine akatar.
    with open("hafta1.txt","r") as f: 
        icerik = f.read()

    # Kücük büyük harf ayrımı olabileceginden lower fonksiyonu ile kücük harfe dönüstürüldü.
    icerik=icerik.lower() 
    # Metin iciinde istemedigimiz karakterleri noktalama isaretleri icerisine ekleyebiliriz.
    noktalama_isaretleri=",.;:?!\n\t"

    # İstenmeyen noktalama isaretleri temizleniyor.
    for isaret in noktalama_isaretleri:
        icerik=icerik.replace(isaret," ")
    
    sayac={}

    # Split fonksiyonu ile metinler bosluklardan ayrılarak kelime haline getiriliyor.
    kelimeler = icerik.split()

    # Her kelime icin daha önce kontraol ettik mi ? 
    # Eger daha önce bu kelimeyi kontrol etmediysek 1,  ettiysekte 1 arttırıyoruz.
    # Bu sekilde bir kelimenin kac defa gectigini buluyor olacagiz.
    for kelime in kelimeler:
        if kelime in sayac:
            sayac[kelime] += 1
        else:
            sayac[kelime]=1

    liste=[]
    # Listeye kelime ve o kelimenin sayisini ekleme
    for value in sayac:
        liste.append([value,sayac[value]])

    # Bubble Sort algoritmasini sıralama icin kullandık
    uzunluk=len(liste)
    for i in range(uzunluk-1):
        for j in range(uzunluk-i-1):
            if liste[j][1] > liste[j+1][1]: #

                liste[j],liste[j+1] = liste[j+1],liste[j]
    
    return liste
   

def dosyaya_yazdirma(liste):
    # Yaptıklarımızı dosyaya yazdırma islemi 
    with open("hafta1_cevap.txt","w") as f:
        for kelime,value in liste:
            if value > 1:
                f.write(kelime + ":" + str(value) + "\n")  
                print(kelime , ":" , value) 

# Degiskene atıp yazdırdık.
sirali_liste = en_cok_tekrar_eden_kelime()
dosyaya_yazdirma(sirali_liste)
print("islem tamamlandi.")


