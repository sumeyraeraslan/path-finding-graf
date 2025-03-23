# path-finding-graf

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

**BFS KODUM:**
https://github.com/sumeyraeraslan/path-finding-graf/blob/b9e6e053127193b92c6abbf80cf0b120eef73139/S%C3%BCmeyraEraslan_MetroSimulation.py#L32-L55

# A* Algoritması Nasıl Çalışır?


