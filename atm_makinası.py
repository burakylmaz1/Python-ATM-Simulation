print("""
*************************************
ATM MAKİNASI

İŞEMLER:

1.BAKİYE SORGULAMA

2.PARA YATIRMA

3.PARA ÇEKME
*************************************

""")

bakiye=1000

while True:

    islem=(input("işlemi giriniz:"))
    if(islem=="q"):
        print("YİNE BEKLERİZ.")
        break
    elif(islem=="1"):
        print("BAKİYENİZ {} TL DİR:".format(bakiye))
    elif(islem=="2"):
        miktar=int(input("MİKTAR GİRİNİZ:"))
        bakiye += miktar
    elif(islem=="3"):
        miktar=int(input("ÇEKMEK İSTEDİĞİNİZ MİKTAR:"))

        if(bakiye-miktar<0):
            print("BAKİYE YETERSİZ")
            continue
        bakiye-=miktar
    else:
        print("GEÇERSİZ İŞLEM.")









