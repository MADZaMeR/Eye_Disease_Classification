# Derin Öğrenme ile Göz Hastalığı Tespiti

Bu depo, derin öğrenme tekniklerini kullanarak göz hastalıklarını tespit eden bir Jupyter Notebook içermektedir. Modelimizi eğitmek ve değerlendirmek için Kaggle'dan [Retina Hastalığı Sınıflandırma veri seti](https://www.kaggle.com/datasets/andrewmvd/retinal-disease-classification/) kullanıyoruz.

## Özellikler

- **Veri Ön İşleme**: Retina görüntülerinin yüklenmesi ve normalizasyon, veri artırma gibi ön işlemlerden geçirilmesi.
- **Model Mimarisi**: TensorFlow ve Keras kullanarak Konvolüsyonel Sinir Ağları (CNN) uygulaması.
- **Eğitim**: Erken durdurma ve öğrenme hızı ayarlama gibi teknikler kullanılarak modelin eğitilmesi.
- **Değerlendirme**: Eğitilen modelin doğruluk, kesinlik, geri çağırma ve F1 skoru gibi çeşitli metriklerle performansının değerlendirilmesi.
- **Görselleştirme**: Eğitim süreci ve model tahminlerinin karışıklık matrisi ve ROC eğrileri ile görselleştirilmesi.

## Başlarken

1. **Depoyu klonlayın**:
    ```bash
    git clone https://github.com/kullaniciadiniz/Eye_Disease_Classification.git
    ```
**Gerekli bağımlılıkları yükleyin**

2. **Jupyter Notebook'u çalıştırın**:
    Notebook'u açın ve verileri ön işleme, modeli eğitme ve performansını değerlendirme adımlarını izleyin.

## Veri Seti

Bu projede kullanılan veri seti, retina görüntülerinin çeşitli hastalık sınıflarına ayrıldığı [Retina Hastalığı Sınıflandırma veri seti](https://www.kaggle.com/datasets/andrewmvd/retinal-disease-classification/)dir. Veri setini indirip uygun dizine yerleştirdiğinizden emin olun.

## Örnek Kullanım Kodu

Bir görüntüyü yükleyip modelle tahmin yapmak için örnek bir kod parçası(RCD.py) bulunmaktadır.
