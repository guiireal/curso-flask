from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import mysql

class ProductIndexController(MethodView):
    def get(self):
        with mysql.cursor() as cursor:
            cursor.execute('SELECT * FROM products')
            products = cursor.fetchall()
        return render_template('public/product/index.html', products=products)

    def post(self):
        name = request.form['name']
        value = request.form['value']
        stock = request.form['stock']
        category_id = request.form['category_id']

        with mysql.cursor() as cursor:
            cursor.execute('INSERT INTO products (name, value, stock, category_id) VALUES (%s, %s, %s, %s)', (name, value, stock, category_id))
            cursor.connection.commit()

        return redirect('/products')
    
class ProductDestroyController(MethodView):
    def post(self, id):
        with mysql.cursor() as cursor:
            cursor.execute('DELETE FROM products WHERE id = %s', (id))
            cursor.connection.commit()
        return redirect('/products')
    
class ProductEditController(MethodView):
    def get(self, id):
        with mysql.cursor() as cursor:
            cursor.execute("SELECT * FROM products WHERE id = %s", (id))
            product = cursor.fetchone()
        return render_template('public/product/edit.html', product=product)
    
    def post(self, id):
        name = request.form['name']
        value = request.form['value']
        stock = request.form['stock']
        category_id = request.form['category_id']

        with mysql.cursor() as cursor:
            cursor.execute('UPDATE products SET name = %s, value = %s, stock = %s, category_id = %s WHERE id = %s', (name, value, stock, category_id, id))
            cursor.connection.commit()

        return redirect('/products')