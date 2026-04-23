# Retail Data Pipeline

## English

### About the Project

Retail Data Pipeline is an autonomous ETL (Extract, Transform, Load) process that generates, cleans, and exports retail e-commerce sales data. The pipeline creates a synthetic dataset, identifies and removes invalid records (zero price or zero quantity), and outputs both raw and cleaned datasets as CSV files.

### Tech Stack

- **Python 3.x**
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical operations and random data generation

### How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the pipeline:

```bash
python data_pipeline.py
```

3. Output files will be generated in the project directory:
   - `raw_sales_data.csv` — Original dataset with erroneous rows
   - `clean_sales_data.csv` — Cleaned dataset ready for analysis

---

## Türkçe

### Proje Hakkında

Retail Data Pipeline, perakende e-ticaret satış verilerini oluşturan, temizleyen ve dışa aktaran otonom bir ETL (Çıkar, Dönüştür, Yükle) sürecidir. Bu veri hattı sentetik bir veri seti oluşturur, geçersiz kayıtları (sıfır fiyat veya sıfır adet) tespit edip kaldırır ve hem ham hem de temizlenmiş veri setlerini CSV dosyaları olarak çıktı verir.

### Kullanılan Teknolojiler

- **Python 3.x**
- **Pandas** — Veri manipülasyonu ve analizi
- **NumPy** — Sayısal işlemler ve rastgele veri üretimi

### Nasıl Çalıştırılır

1. Bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

2. Veri hattını çalıştırın:

```bash
python data_pipeline.py
```

3. Çıktı dosyaları proje dizininde oluşturulacaktır:
   - `raw_sales_data.csv` — Hatalı satırları içeren orijinal veri seti
   - `clean_sales_data.csv` — Analiz için hazır temizlenmiş veri seti
