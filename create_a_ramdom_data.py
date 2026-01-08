import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. VERİ OLUŞTURMA (Data Creation)
# Gerçek hayatta bu veriyi excel veya csv'den okursunuz. 
# Burada pratik yapmak için rastgele veri üretiyoruz.

np.random.seed(42) # Sonuçların her seferinde aynı çıkması için sabitliyoruz
gun_sayisi = 100

data = {
    'Tarih': pd.date_range(start='2024-01-01', periods=gun_sayisi),
    'Kategori': np.random.choice(['Elektronik', 'Giyim', 'Ev & Yaşam', 'Kitap'], gun_sayisi),
    'Satis_Adedi': np.random.randint(1, 20, gun_sayisi),
    'Birim_Fiyat': np.random.randint(50, 1000, gun_sayisi),
    'Musteri_Puani': np.random.uniform(3.0, 5.0, gun_sayisi) # 3.0 ile 5.0 arası puan
}

df = pd.DataFrame(data)

# 2. VERİ ÖN İŞLEME (Data Preprocessing)
# Toplam tutarı hesaplayan yeni bir sütun ekleyelim
df['Toplam_Tutar'] = df['Satis_Adedi'] * df['Birim_Fiyat']

print("--- Veri Setinin İlk 5 Satırı ---")
print(df.head())

print("\n--- Veri Seti Hakkında Genel Bilgi ---")
print(df.info())

print("\n--- İstatistiksel Özet ---")
print(df.describe())

# 3. VERİ ANALİZİ (Data Analysis)
# Kategorilere göre toplam satış tutarlarını bulalım
kategori_ozeti = df.groupby('Kategori')['Toplam_Tutar'].sum().reset_index()
print("\n--- Kategorilere Göre Toplam Satış ---")
print(kategori_ozeti)

# 4. VERİ GÖRSELLEŞTİRME (Data Visualization)
# Grafikleri daha estetik hale getirelim
sns.set_theme(style="whitegrid")
plt.figure(figsize=(15, 10))

# Grafik 1: Kategori Bazlı Toplam Satış (Bar Grafiği)
plt.subplot(2, 2, 1)
sns.barplot(x='Kategori', y='Toplam_Tutar', data=kategori_ozeti, palette='viridis', hue='Kategori', legend=False)
plt.title('Kategorilere Göre Toplam Satış Tutarı')
plt.xlabel('Kategori')
plt.ylabel('Toplam Tutar (TL)')

# Grafik 2: Müşteri Puanlarının Dağılımı (Histogram)
plt.subplot(2, 2, 2)
sns.histplot(df['Musteri_Puani'], bins=15, kde=True, color='orange')
plt.title('Müşteri Puanı Dağılımı')
plt.xlabel('Puan')
plt.ylabel('Frekans')

# Grafik 3: Satış Adedi ile Birim Fiyat İlişkisi (Scatter Plot)
plt.subplot(2, 2, 3)
sns.scatterplot(x='Birim_Fiyat', y='Satis_Adedi', data=df, hue='Kategori', s=100)
plt.title('Fiyat ve Satış Adedi İlişkisi')
plt.xlabel('Birim Fiyat')
plt.ylabel('Satış Adedi')

# Grafik 4: Zaman İçindeki Satış Değişimi (Line Plot)
plt.subplot(2, 2, 4)
# Aylık olarak yeniden örnekleyelim (resample) ki grafik daha okunaklı olsun
df_zaman = df.set_index('Tarih').resample('M')['Toplam_Tutar'].sum().reset_index()
sns.lineplot(x='Tarih', y='Toplam_Tutar', data=df_zaman, marker='o', color='red')
plt.title('Aylık Toplam Satış Trendi')
plt.xlabel('Tarih')
plt.ylabel('Toplam Satış')

plt.tight_layout() # Grafikler birbirine girmesin diye düzenler
plt.show()