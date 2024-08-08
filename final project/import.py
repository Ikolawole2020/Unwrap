import csv
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from unwrap import db,app
from unwrap.models import Products


def main():
    f = open("products.csv")
    reader = csv.reader(f)
    for name, price, description in reader:
    	product = Products(name=name,price=price,description=description)
    	db.session.add(product)
    	print(f"Added product {name}, {price}, {description}")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        main()