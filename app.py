from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    {"id": 1, "author": "Haruki Murakami", "language": "English", "title": "Norwegian Wood"},
    {"id": 2, "author": "Jane Austen", "language": "English", "title": "Pride and Prejudice"},
    {"id": 3, "author": "Gabriel García Márquez", "language": "Spanish", "title": "One Hundred Years of Solitude"},
    {"id": 4, "author": "Fyodor Dostoevsky", "language": "Russian", "title": "Crime and Punishment"},
    {"id": 5, "author": "J.K. Rowling", "language": "English", "title": "Harry Potter and the Sorcerer's Stone"},
    {"id": 6, "author": "Kazuo Ishiguro", "language": "English", "title": "Never Let Me Go"},
    {"id": 7, "author": "George Orwell", "language": "English", "title": "1984"},
    {"id": 8, "author": "Leo Tolstoy", "language": "Russian", "title": "War and Peace"},
    {"id": 9, "author": "Ernest Hemingway", "language": "English", "title": "The Old Man and the Sea"},
    {"id": 10, "author": "Toni Morrison", "language": "English", "title": "Beloved"}
]


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Nothing Found', 404
    if request.method == 'POST':
        new_author = request.form['author']
        new_language = request.form['language']
        new_title = request.form['title']
        id = books_list[-1]['id'] + 1
        new_obj = {
            'id': id,
            'author': new_author,
            'language': new_language,
            'title': new_title
        }
        books_list.append(new_obj)
        return jsonify(books_list), 201

if __name__ == '__main__':
    app.run(debug=True)