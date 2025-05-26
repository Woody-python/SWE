from flask import Flask, render_template, request
import csv 
import time

app = Flask(__name__)

def load_books_from_csv():
    books = []
    with open('books.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

@app.route('/')
def index():
    print('Index Called')
    return render_template('index.html')

@app.route('/books')
def books():
    books = load_books_from_csv()
    return render_template('books.html', books=books)

@app.route('/borrow')
def borrow():
    title = request.args.get('title')
    user_ip = request.remote_addr
    return render_template('borrow.html', title=title, user_ip=user_ip)

