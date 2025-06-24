![Image](https://github.com/user-attachments/assets/0e5d12b6-74cd-46a4-a5e8-5e85255a0654)
# ✈️ Airline Passenger Satisfaction Data Analysis

Bu proje, bir havayolu şirketine ait yolcu verileri üzerinde temel veri analizi, veri temizleme ve görselleştirme çalışmalarını kapsamaktadır. Amaç, yolcu memnuniyetine etki eden faktörleri belirlemek ve istatistiksel çıkarımlarla desteklemektir.

## 📂 Veri Seti

- Kaynak: Airline Passenger Satisfaction (hypothetical/public dataset)
- Gözlem sayısı: 103.904
- Değişkenler: Yaş, Uçuş mesafesi, Gecikme süreleri, Hizmet puanlamaları (1–5), Cinsiyet, Sınıf, Seyahat tipi vb.

## 🔍 Yapılan Analizler

### 1. Eksik Değer Analizi

- Sadece `Arrival Delay in Minutes` değişkeninde %0.3 oranında eksik değer tespit edildi.
- Dağılım çarpık olduğu için **medyan ile doldurma** tercih edildi.

### 2. Aykırı Değer Tespiti

- Boxplot görselleriyle `Departure Delay`, `Flight Distance` ve `Checkin Service` gibi sütunlarda yoğun aykırı değer bulundu.
- Bunlar analiz sürecinde işaretlenerek yorumlandı.

### 3. Değişken Tipi Ayırma

- **Sayısal Değişkenler**: Age, Flight Distance, Delay süreleri
- **Kategorik Değişkenler**: Gender, Satisfaction, Customer Type, Service Ratings (1–5 aralığındaki puanlamalar)

### 4. Betimleyici İstatistikler

- Ortalama, medyan, min-maks, standart sapma ve IQR değerleri `describe()` fonksiyonuyla çıkartıldı.
- Medyan değerler dağılım çarpıklıklarını anlamada kullanıldı.

### 5. Veri Görselleştirme

- Histogram ve boxplot: Sayısal değişkenlerin dağılım ve aykırıları.
- Countplot: Kategorik değişkenlerin frekansları.
- İlişkisel grafikler: Örneğin `Satisfaction` – `Flight Distance` boxplot.

- ![Image](https://github.com/user-attachments/assets/3197d678-30dd-4fb2-81a8-d5ec18aa3225)

## 📅 Kullanılan Araçlar

- Python (Pandas, Matplotlib, Seaborn)
- Jupyter Notebook / PyCharm

## 🚀 Çıktı ve Sonuç

Veri seti genel olarak tutarlı olsa da gecikme süreleri gibi bazı değişkenlerde yoğun uç değer mevcuttu.

Eksik değer oranı düşüktü ve uygun şekilde medyan ile dolduruldu.

Sayısal ve kategorik değişkenler doğru bir şekilde ayrılarak, uygun grafik türleri ile görselleştirildi.

Veri üzerinde yapılan bu ön analiz, sonraki aşamalarda yapılacak makine öğrenmesi modellemesi için güçlü bir zemin hazırlamaktadır.

Veri seti başarılı şekilde temizlenmiş, aykırı ve eksik değerler tespit edilmiş, uygun istatistiksel yöntemlerle yorumlanmıştır. Proje, ileri düzey modelleme çalışmaları için sağlam bir temel oluşturmaktadır.


---



## 📃 Lisans

Bu proje kişisel eğitim ve portföy amacıyla gerçekleştirilmiştir.

