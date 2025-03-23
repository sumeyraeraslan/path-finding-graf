# path-finding-graf

## collections Modülü ##
Modülün önemli amacı, kodumuzu daha okunabilir hale getirmek ve bazı ekstra türlerle veri işlemeyi basitleştirmektir.

  `collections.defaultdict` <br/> 
    <hr> `collections.defaultdict`, Python'da sözlüklerle çalışırken oldukça kullanışlı bir araçtır. Normal bir `dict` yapısında, var olmayan bir anahtara erişmeye çalıştığınızda bir **KeyError** hatası alırsınız. Ancak `defaultdict` kullanırsanız, var olmayan bir anahtara erişmeye çalıştığınızda, bu anahtar için otomatik olarak bir varsayılan değer oluşturur ve bu sayede hata almadan işleminize devam edebilirsiniz.
   **Peki ben nerede kullandım?** <br/>
   `collections.defaultdict`, MetroAgi sınıfının hatlar özelliğini tanımlarken kullanıldım. Hat adı eğer listede yoksa otomatik olarak boş bir liste oluşturucak. <br/> <br/>
   https://github.com/sumeyraeraslan/path-finding-graf/blob/84d3f541c002ec8f79214e4489763ee4135e7d4a/S%C3%BCmeyraEraslan_MetroSimulation.py#L15-L18 <br/>

   Aşağıda gördüğünüz kodda da `defaultdict`, `istasyon_ekle` metodunda kullanılmıştır. `self.hatlar[hat].append(istasyon)` ifadesiyle de, hatlar sözlüğünde hat anahtarına karşılık gelen listeye istasyon'u eklemiş olduk. Eğer hat anahtarını sözlükte bulamazsa, defaultdict otomatik olarak bu anahtar için boş bir liste oluşturur ve istasyon'u bu listeye ekler.

https://github.com/sumeyraeraslan/path-finding-graf/blob/97a21b392daf4b9682c1daa866f303a807206101/S%C3%BCmeyraEraslan_MetroSimulation.py#L20-L24

## collections.deque ##

## heapq ##
`heapq`, Python'da bir öncelik kuyruğu oluşturmak için kullanılan bir modüldür. bu özellikle, **en küçük elemana hızlı erişip**
