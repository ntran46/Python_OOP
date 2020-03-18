# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-03-16


from flask import Flask, jsonify, request, make_response
from library_manager import LibraryManager
from textbook import Textbook
from ebook import eBook

app = Flask(__name__)

library = LibraryManager("Maryam")


@app.route("/library_manager/<book_type>", methods=["POST"])
def add_book(book_type):
    data = request.json
    try:
        if book_type == "textbook":
            textbook = Textbook(data["id"], data["title"], data["author"],
                                data["published_year"], data["edition"],
                                data["cover_type"], data["subject"], data["is_borrowed"])
            library.add_book(textbook)

        elif book_type == "ebook":
            ebook = eBook(data["id"], data["title"], data["author"],
                          data["published_year"], data["edition"],
                          data["platform"], data["genre"], data["is_borrowed"])
            library.add_book(ebook)

        return make_response(data["id"], 200)
    except ValueError as error:
        message = str(error)
        return make_response(message, 400)


@app.route("/library_manager/<book_type>/<book_id>", methods=["PUT"])
def update_book(book_id, book_type):
    data = request.json
    book = library.get_book_by_id(book_id)

    if not book:
        return make_response("Textbook not found.", 404)

    if book_type == "textbook":
        if "subject" not in data.keys():
            return make_response("Invalid JSON: missing subject", 400)
        if "cover_type" not in data.keys():
            return make_response("Invalid JSON: missing cover type", 400)

    if book_type == "ebook":
        if "platform" not in data.keys():
            return make_response("Invalid JSON: missing platform", 400)
        if "genre" not in data.keys():
            return make_response("Invalid JSON: missing genre", 400)

    try:
        if book_type == "textbook":
            library.update_book(book_id, data["subject"], data["cover_type"])
        elif book_type == "ebook":
            library.update_book(book_id, data["platform"], data["genre"])

        return make_response("", 200)
    except ValueError as error:
        return make_response(str(error), 400)


@app.route("/library_manager/book/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    try:
        library.remove_book(book_id)
    except ValueError as error:
        return make_response(str(error), 400)
    else:
        return make_response("", 200)


@app.route("/library_manager/all", methods=["GET"])
def list_books():
    return make_response(jsonify(library.to_dict()), 200)


@app.route("/library_manager/book/<book_id>", methods=["GET"])
def get_book_by_id(book_id):
    book = library.get_book_by_id(book_id)

    if not book:
        return make_response("Book not found.", 404)
    try:
        return make_response(jsonify(library.get_book_by_id(book_id).to_dict()), 200)

    except AttributeError as error:
        return make_response(str(error), 404)


@app.route("/library_manager/all/<book_type>", methods=["GET"])
def get_book_by_type(book_type):
    book = library.get_books_by_type(book_type)
    if not book:
        return make_response("Book not found.", 404)

    return make_response(jsonify(library.get_books_by_type(book_type)), 200)


@app.route("/library_manager/all/stats", methods=["GET"])
def get_book_stats():
    return make_response(jsonify(library.get_book_stat().to_dict()), 200)


@app.route("/validate", methods=["GET", "POST", "PUT", "DELETE"])
def validate_setup():
    return jsonify(
        {
            "method": request.method,
            "Content-Type header": request.headers.get("Content-Type"),
            "data": request.data.decode(),
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
