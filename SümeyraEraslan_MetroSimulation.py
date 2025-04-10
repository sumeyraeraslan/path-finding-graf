from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str,koordinatlar: Tuple[int, int] = (0, 0)):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları
        self.koordinatlar = koordinatlar  # (x, y) koordinatları
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre)
        
    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str,koordinatlar: Tuple[int, int] = (0, 0)) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat, koordinatlar)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def heuristic(self, istasyon1: Istasyon, istasyon2: Istasyon) -> int:

        x1, y1 = istasyon1.koordinatlar # istasyon1'in koordinatlarını aldık
        x2, y2 = istasyon2.koordinatlar # istasyon2'in koordinatlarını aldık
        return abs(x1 - x2) + abs(y1 - y2) #Mesafe hesaplama
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar: #Eğer başlangıç değeri grafin içinde değilse
            return None 

        baslangic= self.istasyonlar[baslangic_id]
        hedef= self.istasyonlar[hedef_id]

        queue=deque([(baslangic,[baslangic])])
        visited=set([baslangic])

        while queue:
            mevcut_istasyon,yol=queue.popleft()
        #Bir önceki adımda ziyaret edilen yapıyı visited'a atmıştık
        #Şimdi ise ziyaret edilmiş ve kuyruğun yapısında duran istasyonu kuyruktan atıyoruz.

            if mevcut_istasyon== hedef: # Eğer mevcut istasyonumuz hedef id'mize eşit ise yolu döndür
                return yol 

            for komsu, _ in mevcut_istasyon.komsular: #Ziyaret edilmiş istasyonlardaki komşu istasyonlara bakmak için döngüye aldık
                if komsu.idx not in visited: #Eğer komşu istasyonlardaki bir istasyon ziyaret edilmemişse git ve ziyaret et demek istiyor.
                    visited.add(komsu)#Ziyaret edilen istasyonu visited'a ekle
                    queue.append((komsu,yol+[komsu])) #Kuyruk yapısında yeni yolu güncelledik.

        return None 


    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic= self.istasyonlar[baslangic_id] #Değişkene atama
        hedef= self.istasyonlar[hedef_id]

        pq = [(0 + self.heuristic(baslangic, hedef),0, id(baslangic.idx), baslangic, [baslangic])] #Kuyruk yapısı= başlangıç süresi, istasyonun id'si, mevcut istasyon, şu ana kadar izlenen yol
        ziyaret_edildi = set()

        while pq:
            f,sure, _, mevcut, yol = heapq.heappop(pq) #heapq.heappop() ile en düşük süreye sahip yolu buluyoruz

            if mevcut in ziyaret_edildi: # ziyaret edildiyse devam et
                continue
            ziyaret_edildi.add(mevcut)

            if mevcut == hedef: #Mevcut istasyon hedefe ulaştıysa şuana kadar izlenen yolu ve süreyi döndürür
                return yol, sure

            for komsu, gecis_suresi in mevcut.komsular:
                if komsu not in ziyaret_edildi: #Daha önce ziyaret edilmediyse 
                    yeni_sure = sure + gecis_suresi # Var olan süreyle geçiş süresini topla ve yeni süreye aktar.
                    f = yeni_sure + self.heuristic(komsu, hedef)
                    heapq.heappush(pq,(f, yeni_sure, id(komsu), komsu, yol + [komsu])) #heapq ile veriler, küçükten büyüğe sıralanır.
                    #Tahmini değer, son süre değeri, şu anda değerlendirilen komşu düğüm, bu düğüme kadar gidilen yol + son eklenen düğüm değeri
        return None

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat",(0,0))
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat",(1,1))
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat",(2,2))
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat",(3,3))
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat",(5,5))
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat",(3,3))
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat",(4,4))  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat",(5,5))  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat",(6,6))
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 
