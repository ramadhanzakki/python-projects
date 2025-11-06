# File: read_question.py

import csv
import os

# Baris ini akan mendapatkan path absolut ke folder tempat proyek Anda berada
# (yaitu, folder 'Quiz_game')
project_root_dir = os.path.dirname(os.path.abspath(__file__))

def read_questions_from_csv(relative_filepath):
    """
    Membaca file CSV dari path relatif terhadap folder utama proyek.
    Contoh: 'question_list/geography.csv'
    """
    
    # Menggabungkan path root proyek dengan path relatif file
    # Ini akan menciptakan path yang lengkap dan benar, contoh:
    # D:/.../Quiz_game/question_list/geography.csv
    absolute_file_path = os.path.join(project_root_dir, relative_filepath)
    
    questions = []
    try:
        with open(absolute_file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                questions.append(row)
    except FileNotFoundError:
        print(f"--> FATAL ERROR: File tidak ditemukan!")
        print(f"--> Python mencoba mencari di path ini: {absolute_file_path}")
        print(f"--> Pastikan path '{relative_filepath}' sudah benar di main.py dan file-nya ada.")
        return [] # Kembalikan list kosong agar tidak crash
        
    return questions