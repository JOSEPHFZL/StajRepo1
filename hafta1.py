def en_cok_tekrar_eden_kelime():
    with open("hafta1.txt","r") as f:
        icerik = f.read()

    icerik=icerik.lower()
    yeni_icerik = icerik.split()

    kelimeler={}

    for kelime in yeni_icerik:
        if kelime in kelimeler:
            kelimeler[kelime] += 1
        else:
            kelimeler[kelime]=1

    max_kelime=1
    en_cok_tekrar_eden = ""

    for i in kelimeler: 
        if kelimeler[i] > max_kelime :
            max_kelime=kelimeler[i]
            en_cok_tekrar_eden=i
    
    
    with open("hafta1_cevap.txt","w") as f:
        f.write("En çok tekrar eden kelime : " + en_cok_tekrar_eden + "\n")
        f.write("Gecme sayisi: " + str(max_kelime))

    return f"En çok tekrar eden kelime : {en_cok_tekrar_eden} = {max_kelime}'dir."  

print(en_cok_tekrar_eden_kelime())

