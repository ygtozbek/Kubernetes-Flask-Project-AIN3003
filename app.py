from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# --- Veritabani Ayarlari ---
# Proje dosyasinda admin/admin olacak diye
mongo_host = os.environ.get('MONGO_HOST', 'localhost')
mongo_user = os.environ.get('MONGO_USERNAME', 'admin')
mongo_pass = os.environ.get('MONGO_PASSWORD', 'admin')


client = MongoClient(f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:27017/")

# Database ismi BOOKSTORE olacak
db = client['BOOKSTORE']
col = db['books'] 

@app.route('/')
def home():
    return "Hello! AIN-3003 Project 1 is Running!"

# 1. KITAP EKLEME
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    print("Gelen veri:", data) # Veri geliyor mu diye bakiyorum

    # Title ve Author zorunlu alanlar
    if 'title' not in data:
        return jsonify({"error": "Title eksik!"}), 400
    
    if 'author' not in data:
        return jsonify({"error": "Author eksik!"}), 400

    # Yil yoksa 2025 
    year = 2025
    if 'year' in data:
        year = data['year']

    new_book = {
        "title": data['title'],
        "author": data['author'],
        "year": year
    }
    
    # Kaydetme 
    col.insert_one(new_book)
    return jsonify({"message": "Book added successfully"}), 201

# 2. LISTELEME
@app.route('/books', methods=['GET'])
def get_books():
    books = []
    
    # Veritabanindaki tüö kitapları donup listeye eklemek için
    for doc in col.find():
        temp = {
            "title": doc['title'],
            "author": doc['author'],
            "year": doc.get('year')
        }
        books.append(temp)
    
    print(f"Toplam {len(books)} kitap bulundu")
    return jsonify(books), 200

# 3. GUNCELLEME
@app.route('/books/<title>', methods=['PUT'])
def update_book(title):
    data = request.get_json()
    print("Guncelleniyor:", title)
    
    # Sadece gelen alanlari guncelle ($set ile)
    result = col.update_one({"title": title}, {"$set": data})
    
    if result.matched_count > 0:
        return jsonify({"message": "Book updated"}), 200
    else:
        return jsonify({"error": "Book not found"}), 404

# 4. SILME
@app.route('/books/<title>', methods=['DELETE'])
def delete_book(title):
    print("Siliniyor:", title)
    result = col.delete_one({"title": title})
    
    if result.deleted_count > 0:
        return jsonify({"message": "Book deleted"}), 200
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    # Docker icin host 0.0.0.0 
    app.run(host='0.0.0.0', port=5000, debug=True)