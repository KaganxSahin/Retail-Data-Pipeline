"""
# Data Pipeline Script for Retail E-Commerce Sales Data
# E-Ticaret Satış Verileri için Veri Hattı Scripti

# This script generates a dummy e-commerce sales dataset,
# cleans erroneous rows, and outputs a clean dataset.
# Bu script, örnek bir e-ticaret satış veri seti oluşturur,
# hatalı satırları temizler ve temiz bir veri seti çıktısı verir.
"""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
# Tekrarlanabilirlik için rastgele tohum değeri ayarla
np.random.seed(42)


def generate_dummy_dataset(n_rows=100):
    """
    # Generate a dummy e-commerce sales dataset with n_rows rows.
    # n_rows satırlık örnek bir e-ticaret satış veri seti oluşturur.

    # Some rows will intentionally have price=0 or quantity=0 to simulate dirty data.
    # Kirli veriyi simüle etmek için bazı satırlar kasıtlı olarak fiyat=0 veya adet=0 içerecektir.
    """

    # Define product categories and product names
    # Ürün kategorilerini ve ürün isimlerini tanımla
    categories = ["Electronics", "Clothing", "Home & Garden", "Sports", "Books"]
    products = {
        "Electronics": ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"],
        "Clothing": ["T-Shirt", "Jeans", "Jacket", "Sneakers", "Hat"],
        "Home & Garden": ["Lamp", "Pillow", "Vase", "Rug", "Curtain"],
        "Sports": ["Yoga Mat", "Dumbbell", "Basketball", "Tennis Racket", "Jump Rope"],
        "Books": ["Novel", "Textbook", "Cookbook", "Biography", "Comic"],
    }

    # Define cities for customer location
    # Müşteri lokasyonu için şehirleri tanımla
    cities = ["Istanbul", "Ankara", "Izmir", "Bursa", "Antalya"]

    # Generate random data for each column
    # Her sütun için rastgele veri oluştur
    data = {
        "order_id": range(1001, 1001 + n_rows),
        "customer_id": np.random.randint(1, 51, size=n_rows),
        "category": np.random.choice(categories, size=n_rows),
        "city": np.random.choice(cities, size=n_rows),
        "quantity": np.random.randint(0, 10, size=n_rows),  # 0 included intentionally / 0 kasıtlı olarak dahil
        "unit_price": np.round(np.random.uniform(0, 500, size=n_rows), 2),  # 0 included intentionally / 0 kasıtlı olarak dahil
        "order_date": pd.date_range(start="2025-01-01", periods=n_rows, freq="D"),
    }

    df = pd.DataFrame(data)

    # Assign product names based on category
    # Kategoriye göre ürün isimlerini ata
    df["product"] = df["category"].apply(lambda cat: np.random.choice(products[cat]))

    # Calculate total price for each order
    # Her sipariş için toplam fiyatı hesapla
    df["total_price"] = np.round(df["quantity"] * df["unit_price"], 2)

    # Inject some explicitly bad rows: set some prices and quantities to 0
    # Kasıtlı olarak hatalı satırlar ekle: bazı fiyat ve adetleri 0 yap
    bad_indices = np.random.choice(df.index, size=10, replace=False)
    df.loc[bad_indices[:5], "unit_price"] = 0.0
    df.loc[bad_indices[5:], "quantity"] = 0

    # Recalculate total_price after injecting bad data
    # Hatalı veri eklendikten sonra toplam fiyatı yeniden hesapla
    df["total_price"] = np.round(df["quantity"] * df["unit_price"], 2)

    return df


def clean_dataset(df):
    """
    # Remove rows where unit_price is 0 or quantity is 0.
    # Birim fiyatı 0 veya adedi 0 olan satırları kaldırır.

    # These rows represent invalid/erroneous transactions.
    # Bu satırlar geçersiz/hatalı işlemleri temsil eder.
    """

    # Count rows before cleaning
    # Temizleme öncesi satır sayısını say
    initial_count = len(df)

    # Filter out rows with zero price or zero quantity
    # Fiyatı sıfır veya adedi sıfır olan satırları filtrele
    df_clean = df[(df["unit_price"] > 0) & (df["quantity"] > 0)].copy()

    # Count rows after cleaning
    # Temizleme sonrası satır sayısını say
    final_count = len(df_clean)

    # Report how many rows were removed
    # Kaç satırın kaldırıldığını raporla
    removed = initial_count - final_count
    print(f"[INFO] Removed {removed} invalid rows ({initial_count} -> {final_count})")
    print(f"[BİLGİ] {removed} geçersiz satır kaldırıldı ({initial_count} -> {final_count})")

    # Reset index after dropping rows
    # Satırlar kaldırıldıktan sonra indeksi sıfırla
    df_clean.reset_index(drop=True, inplace=True)

    return df_clean


def display_summary(df, label="Dataset"):
    """
    # Display basic statistics and info about the dataset.
    # Veri seti hakkında temel istatistikleri ve bilgileri gösterir.
    """

    print(f"\n{'='*60}")
    print(f" {label} Summary / {label} Özeti")
    print(f"{'='*60}")

    # Show shape of the dataframe
    # Veri çerçevesinin boyutlarını göster
    print(f"Shape / Boyut: {df.shape}")

    # Show first 5 rows
    # İlk 5 satırı göster
    print(f"\nFirst 5 rows / İlk 5 satır:\n{df.head()}")

    # Show basic statistics for numeric columns
    # Sayısal sütunlar için temel istatistikleri göster
    print(f"\nStatistics / İstatistikler:\n{df.describe()}")


# ============================================================
# Main execution block
# Ana çalıştırma bloğu
# ============================================================
if __name__ == "__main__":

    # Step 1: Generate the dummy dataset
    # Adım 1: Örnek veri setini oluştur
    print("[STEP 1] Generating dummy e-commerce dataset...")
    print("[ADIM 1] Örnek e-ticaret veri seti oluşturuluyor...")
    raw_df = generate_dummy_dataset(n_rows=100)
    display_summary(raw_df, label="Raw / Ham Veri")

    # Step 2: Clean the dataset
    # Adım 2: Veri setini temizle
    print("\n[STEP 2] Cleaning dataset (removing invalid rows)...")
    print("[ADIM 2] Veri seti temizleniyor (geçersiz satırlar kaldırılıyor)...")
    clean_df = clean_dataset(raw_df)
    display_summary(clean_df, label="Clean / Temiz Veri")

    # Step 3: Save both datasets to CSV
    # Adım 3: Her iki veri setini CSV olarak kaydet
    print("\n[STEP 3] Saving datasets to CSV...")
    print("[ADIM 3] Veri setleri CSV olarak kaydediliyor...")
    raw_df.to_csv("raw_sales_data.csv", index=False)
    clean_df.to_csv("clean_sales_data.csv", index=False)

    print("\n[DONE] Pipeline completed successfully!")
    print("[BİTTİ] Veri hattı başarıyla tamamlandı!")
