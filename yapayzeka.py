import random
import json

class EgitilebilirYapayZeka:
    def __init__(self):
        self.veri_tabani = self.veritabani_yukle()

    def veritabani_yukle(self):
        try:
            with open("veritabani.json", "r") as dosya:
                return json.load(dosya)
        except FileNotFoundError:
            return {}

    def veritabani_kaydet(self):
        with open("veritabani.json", "w") as dosya:
            json.dump(self.veri_tabani, dosya)

    def egit(self, soru, cevap):
        soru = soru.lower()
        if soru in self.veri_tabani:
            self.veri_tabani[soru].append(cevap)
        else:
            self.veri_tabani[soru] = [cevap]
        self.veritabani_kaydet()

    def cevap_ver(self, soru):
        soru = soru.lower()
        if soru in self.veri_tabani:
            cevaplar = self.veri_tabani[soru]
            return random.choice(cevaplar)
        else:
            return "Üzgünüm, bu soruyu henüz öğrenmedim."

def main():
    yapay_zeka = EgitilebilirYapayZeka()
    print("Yapay Zeka: Merhaba! Beni eğitmek için sorular sormaya başlayabilirsiniz. Eğitimi bitirmek için 'çık' yazabilirsin.")

    while True:
        soru = input("Sen: ")
        if soru.lower() == "çık":
            print("Yapay Zeka: Eğitim modundan çıkılıyor.")
            yapay_zeka.veritabani_kaydet()
            break
        cevap = input("Yapay Zeka: Sorunun cevabı nedir? ")
        yapay_zeka.egit(soru, cevap)
        print("Yapay Zeka: Soruyu öğrendim!")

    print("\nYapay Zeka: Eğitim tamamlandı. Artık sorularınızı cevaplayabilirim.")

    while True:
        soru = input("Sen: ")
        if soru.lower() == "çık":
            print("Yapay Zeka: Görüşmek üzere!")
            break
        cevap = yapay_zeka.cevap_ver(soru)
        print("Yapay Zeka:", cevap)

if __name__ == "__main__":
    main()
