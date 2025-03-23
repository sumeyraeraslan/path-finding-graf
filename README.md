# En Hızlı ve En Kısa Yolu Bulma

## 1. collections Modülü ##
Modülün önemli amacı, kodumuzu daha okunabilir hale getirmek ve bazı ekstra türlerle veri işlemeyi basitleştirmektir. <br/> <br/> 

## a) collections.defaultdict ## 
`collections.defaultdict`, Python'da sözlüklerle çalışırken oldukça kullanışlı bir araçtır. Normal bir `dict` yapısında, var olmayan bir anahtara erişmeye çalıştığınızda bir **KeyError** hatası alırsınız. Ancak `defaultdict` kullanırsanız, var olmayan bir anahtara erişmeye çalıştığınızda, bu anahtar için otomatik olarak bir varsayılan değer oluşturur ve bu sayede hata almadan işleminize devam edebilirsiniz. <br/> 
    
   **Peki ben nerede kullandım?** <br/>
   
   `collections.defaultdict`, MetroAgi sınıfının hatlar özelliğini tanımlarken kullanıldım. Hat adı eğer listede yoksa otomatik olarak boş bir liste oluşturucak. <br/> <br/>
   https://github.com/sumeyraeraslan/path-finding-graf/blob/84d3f541c002ec8f79214e4489763ee4135e7d4a/S%C3%BCmeyraEraslan_MetroSimulation.py#L15-L18 

   Aşağıda gördüğünüz kodda da `defaultdict`, `istasyon_ekle` metodunda kullanılmıştır. `self.hatlar[hat].append(istasyon)` ifadesiyle de, hatlar sözlüğünde hat anahtarına karşılık gelen listeye istasyon'u eklemiş olduk. Eğer hat anahtarını sözlükte bulamazsa, defaultdict otomatik olarak bu anahtar için boş bir liste oluşturur ve istasyon'u bu listeye ekler.

https://github.com/sumeyraeraslan/path-finding-graf/blob/97a21b392daf4b9682c1daa866f303a807206101/S%C3%BCmeyraEraslan_MetroSimulation.py#L20-L24

## b) collections.deque ##
`collections.deque`, Python'da **çift uçlu kuyruk (double-ended queue)** veri yapısını sağlayan bir modüldür. Bu veri yapısı, hem baştan hem de sondan ekleme ve çıkarma işlemlerini O(1) karmaşıklığında (yani sabit zaman) gerçekleştirir. Bu özelliği, deque'yi özellikle BFS (Breadth-First Search) gibi algoritmalarda kullanmak için ideal hale getirir.Hem **stack (LIFO - Last In First Out)** hem de **queue (FIFO - First In First Out)** gibi davranabilir.Ama BFS gibi algoritmalarda queue(kuyruk) olarak kullanılır. <br/> 

**Peki ben nerede kullandım?** <br/> 

`collections.deque`, `MetroAgi` sınıfının `en_az_aktarma_bul` metodunda kullandım. En az aktarma bulmak adına **FIFO (First In First Out - İlk Giren İlk Çıkar)** prensibine sahip queue yapısını kullandım. Burda istasyonumuza uğrayarak, istasyonu ziyaret edildi olarak set ettikten sonra queue(kuyruk)'tan atmasını sağladım. `mevcut_istasyon`'da şu ana kadar ziyaret edilen istasyonu temsil eder.

https://github.com/sumeyraeraslan/path-finding-graf/blob/bb97908372be73ff0807cd82c7b926a8fb093a09/S%C3%BCmeyraEraslan_MetroSimulation.py#L32-L55


## 2. heapq ##
`heapq`, Python'da bir öncelik kuyruğu oluşturmak için kullanılan bir modüldür.Bu özellikle, **en küçük elemana hızlı erişip** elemanları sıralı bir şekilde tutmak için kullanıyoruz. `heapq`, bir **min-heap** yapısıdır, yani en küçük eleman her zaman kök(root) konumundadır. <br/> 

**Peki ben nerede kullandım?** <br/> 

heapq, `MetroAgi` sınıfının `en_hizli_rota_bul` metodunda kullandım. Bu algoritmada, en kısa rotaya öncelik verdip en hızlı rotaya ulaşmış olduk.  <br/>  
https://github.com/sumeyraeraslan/path-finding-graf/blob/0c29be74d95bf2ede618c39b5e5843cb46e7e409/S%C3%BCmeyraEraslan_MetroSimulation.py#L58-L82

## 3. typing Modülü
`typing` modülünü, kodun okunabilirliğini artırmak, hata ayıklamayı kolaylaştırmak ve IDE desteğinden daha iyi yararlanmak için kullanılır.

 **Peki ben nerede kullandım?** <br/>

 Aşağıda gördüğünüz koddaki gibi yerlerde belirtilen parametrelerin tiplerini(str,int...) belirtmek için kullanıldı.
https://github.com/sumeyraeraslan/path-finding-graf/blob/4f218ce3119a7fa1bd8ae8a4d239e0936d8e93a3/S%C3%BCmeyraEraslan_MetroSimulation.py#L5-L10

# BFS Algoritması Nasıl Çalışır?
BFS (Breadth-First Search), **bir graf veya ağaç yapısında düğümleri(node) dolaşmak** için kullanılan bir algoritmadır. BFS, **en az aktarmalı veya en kısa yol** gibi problemleri çözmek için idealdir bir algoritmadır. Belirli başlangıç bir düğümden başlayarak, önce başlangıç düğümünün **tüm komşularını** ziyaret eder, ardından bu **komşuların komşularını** ziyaret eder ve bu şekilde tüm grafı katman katman dolaşır. Bu yöntem, queue(kuyruk) veri yapısı kullanılarak gerçekleştirilir ve **FIFO (First In First Out - İlk Giren İlk Çıkar)** prensibine dayanır. BFS, özellikle ağırlıksız graflarda **en kısa yolu** bulmak için kullanılır, çünkü başlangıç düğümünden hedef düğüme giden en az sayıda adımı garanti eder.

**BFS Kodum:**
https://github.com/sumeyraeraslan/path-finding-graf/blob/b9e6e053127193b92c6abbf80cf0b120eef73139/S%C3%BCmeyraEraslan_MetroSimulation.py#L32-L55

# A* Algoritması Nasıl Çalışır?
A* Algoritması, bir graf veya harita üzerinde **en kısa yolu bulmak** için kullanılan bir arama algoritmasıdır. BFS gibi tüm olası yolları keşfetmek yerine, heuristic(sezgisel) bir tahmin kullanarak daha akıllıca bir arama yapar. Bu sayede, özellikle **büyük ve karmaşık yapılarda daha hızlı ve verimli** bir şekilde en kısa yolu bulur. A* algoritması, her bir düğüm için toplam tahmini maliyeti f(n) hesaplar. <br/> 

**-f(n) = g(n) + h(n)** <br/>

Gerçek maliyet '(g)' ile gösterilirken heuristic(sezgisel) maliyet '(h)' ile gösterilir. A* algoritması, her adımda en düşük f(n) değerine sahip düğümü seçer. Bu şekilde, hem gerçek maliyeti hem de hedefe olan tahmini mesafeyi dikkate alarak en verimli yolu bulur.Listeden en düşük f(n) değerine sahip düğümü seçer.Eğer bu düğüm hedef düğümse, algoritmayı sonlandır ve rotayı geriye doğru takip ederek bulur. Eğer değilse seçilen düğümün tüm komşularını gezer. Eğer açık listede değilse veya yeni bir yol daha kısaysa: g değerini günceller, h ve f(n) = g(n) + h(n) değerini hesaplar. Kapalı liste boşalana kadar adımları tekrarlar.

**A * Kodum:**
https://github.com/sumeyraeraslan/path-finding-graf/blob/109d283113cafd8c1e1cf6ae427f2c39c5fe4844/S%C3%BCmeyraEraslan_MetroSimulation.py#L66-L91

# Neden BFS ve A * Algoritması Kullandık?

BFS (Breadth-First Search) ve A* algoritmaları, yol bulma problemlerinde sıkça kullanılan iki farklı algoritmadır.
**BFS algoritma kullanma nedenimiz:**
En az aktarmalı rotayı bulur, basit ve anlaşılırdır ve eğer graf ağırlıksız ise (yani tüm kenarlar eşit maliyete sahipse), BFS her zaman en kısa yolu bulur.
Bu projede BFS kullanma amacımız ise metro ağında, yolcular genellikle en az aktarmalı rotayı tercih etmek ister. Örneğin, bir yolcu A noktasından B noktasına giderken mümkün olduğunca az hat değiştirmek ister. Bu nedenle, BFS algoritması bu tür bir rotayı bulmak için ideal bir algoritmadır. 

**A * algoritmasını kullanma nedenimiz:**
A* algoritması, en hızlı rotayı bulmak için kullanılan bir algoritmadır. Bu projede kullanma amacımız ise metro ağında, yolcular çoğu zaman zamandan tasarruf etmek için en hızlı rotayı tercih etmek ister. En hızlı yolu bulmak için en uygun A* algoritmasıdır.

# Örnek Kullanım ve Test Sonuçları
Örnek kullanım kısmı, MetroAgi sınıfında verilerin girilmesi, sınıfının nasıl kullanılacağını gösteren bir dizi test senaryosu içerir. Bu test senaryoları, programın doğru çalışıp çalışmadığını denetler.
`istasyon_ekle` metodu kullanılarak farklı hatlara ait istasyonlar eklenir. Her istasyonun bir kimliği (idx), adı (ad), hattı (hat) ve koordinatları (koordinatlar) vardır. 
Örneğin:
https://github.com/sumeyraeraslan/path-finding-graf/blob/ef7474b4e3987e8883a98f97a080543116330179/S%C3%BCmeyraEraslan_MetroSimulation.py#L99-L99
`baglanti_ekle` metodu kullanılarak istasyonlar arasındaki bağlantılar ve bu bağlantıların geçiş süreleri belirlenir. En sonda geçtiği rotaların toplam süresini ve bütün geçtiği rotaları yazdırır. 

# Projeyi Geliştirme Fikirleri 
Bu projede ek olarak bir geliştirme yapmadım.Fakat nasıl geliştirilebilirdi sorularına ufakta olsa fikirleri belirtmek ve kaydetmek istedim.

**Nasıl Geliştirilebilirdi?**
İlk olarak büyükşehirlerin yol güzargahları hakkında internetten veri çekebilirdik. Bu verilerle birlikte kullanıcıdan nereden nereye gitmek istediği hakkında bir girdi alabilirdik. Ve kullanıcılar için en uygun malliyetli yolu bulabilirdik. Yolcunun hangi yoldan gitmeyi isteğini filtrelemesini sağlayabilirdik(en hızlı, en kısa, en uygun maliyetli yada hepsi).
