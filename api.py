from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
#9
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/your_database_name"
mongo = PyMongo(app)

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    books = mongo.db.books
    book_id = books.insert(data)
    new_book = books.find_one({"_id": book_id})
    return jsonify({"message": "Book added successfully", "data": new_book}), 201

@app.route("/books", methods=["GET"])
def get_books():
    books = mongo.db.books
    result = []
    for book in books.find():
        result.append({"_id": str(book["_id"]), "title": book["title"], "author": book["author"]})
    return jsonify({"data": result})

@app.route("/books/<id>", methods=["GET"])
def get_book(id):
    books = mongo.db.books
    book = books.find_one({"_id": ObjectId(id)})
    if book:
        return jsonify({"data": {"_id": str(book["_id"]), "title": book["title"], "author": book["author"]}})
    else:
        return jsonify({"message": "Book not found"}), 404

@app.route("/books/<id>", methods=["PUT"])
def update_book(id):
    data = request.get_json()
    books = mongo.db.books
    result = books.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.modified_count > 0:
        return jsonify({"message": "Book updated successfully"})
    else:
        return jsonify({"message": "Book not found"}), 404

@app.route("/test/<id>", methods=["PUT"])
def update_book(id):
    data = request.get_json()
    books = mongo.db.books
    result = books.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.modified_count > 0:
        return jsonify({"message": "Book updated successfully"})
    else:
        return jsonify({"message": "Book not found"}), 404

@app.route("/books/<id>", methods=["DELETE"]) 
def delete_book(id):
    books = mongo.db.books
    result = books.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify({"message": "Book deleted successfully"})
    else:
        return jsonify({"message": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

