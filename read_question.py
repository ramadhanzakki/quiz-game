# File: read_question.py

import csv
import os

# Dapatkan path absolut dari folder tempat script ini berada
script_dir = os.path.dirname(__file__)

def read_questions_from_csv(filename):
    """Membaca pertanyaan dari file CSV menggunakan path absolut yang aman."""
    
    # Gabungkan path folder script dengan nama file yang diberikan
    file_path = os.path.join(script_dir, filename)
    
    questions = []
    try:
        # Buka file menggunakan path yang sudah lengkap dan benar
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                questions.append(row)
    except FileNotFoundError:
        # Berikan pesan error yang lebih membantu jika file tidak ada
        print(f"--> ERROR: File '{filename}' tidak ditemukan di lokasi '{script_dir}'.")
        print("--> Pastikan nama file sudah benar dan berada di folder yang sama dengan script Python.")
        return [] # Kembalikan list kosong agar program tidak crash
        
    return questions