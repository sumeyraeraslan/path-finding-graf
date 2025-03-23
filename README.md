# path-finding-graf

## collections Modülü ##
Modülün önemli amacı, kodumuzu daha okunabilir hale getirmek ve bazı ekstra türlerle veri işlemeyi basitleştirmektir.

   `collections.defaultdict` <br/>
    <hr> `collections.defaultdict`, Python'da sözlüklerle çalışırken oldukça kullanışlı bir araçtır. Normal bir `dict` yapısında, var olmayan bir anahtara erişmeye çalıştığınızda bir **KeyError** hatası alırsınız. Ancak `defaultdict` kullanırsanız, var olmayan bir anahtara erişmeye çalıştığınızda, bu anahtar için otomatik olarak bir varsayılan değer oluşturur ve bu sayede hata almadan işleminize devam edebilirsiniz.<br/> <br/>
   **Peki ben nerede kullandım?** <br/>
   `collections.defaultdict`, MetroAgi sınıfının hatlar özelliğini tanımlarken kullanıldım. Hat adı eğer listede yoksa otomatik olarak boş bir liste oluşturucak. <br/> <br/>
   ![İstasyon Ekleme Kodu](https://github.com/sumeyraeraslan/path-finding-graf/blob/84d3f541c002ec8f79214e4489763ee4135e7d4a/S%C3%BCmeyraEraslan_MetroSimulation.png)

