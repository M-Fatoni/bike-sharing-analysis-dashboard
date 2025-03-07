# 🚴 Bike Rental Analysis Dashboard ✨

Dashboard interaktif ini dibuat untuk menganalisis pola penyewaan sepeda berdasarkan berbagai faktor seperti musim, jam, hari kerja, dan kondisi cuaca.

## 📦 Struktur Direktori

submission
```
submission/
│── dashboard/
│   ├── main_data.csv
│   ├── dashboard.py
│
│── data/
│   ├── data_1.csv
│   ├── data_2.csv
│
│── notebook.ipynb
│── README.md
│── requirements.txt
│── url.txt
```

## ⚙️ Setup Environment

### Menggunakan Anaconda
```

conda create --name bike-rental python=3.9
conda activate bike-rental
pip install -r requirements.txt
```

### Menggunakan Shell/Terminal (Tanpa Anaconda)


```python
mkdir bike_rental_project
cd bike_rental_project
pipenv install
pipenv shell
pip install -r requirements.txt
```

## 🚀 Menjalankan Dashboard Streamlit

streamlit run dashboard/dashboard.py
