#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Categories, Items, Base
# global session
app = Flask(__name__)
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

@app.route('/')
@app.route('/categories/')
def showCategories():
    '''
    Show the home page for of item catalog web
    :param: takes no parameter
    :return: Shows all the categories
    '''
    global session
    categories = session.query(Categories).all()
    return render_template('catalog.html', categories=categories)

@app.route('/categories/<category_id>/items')
def showcategoryItems(category_id):
    '''
    Show the category items on web
    :param: takes category as argument
    :return:return the web page for the category id.
    '''
    global session
    items = session.query(Items).filter_by(category_id=category_id).all()
    return render_template('showcategoriesItems.html', items=items, category_id=category_id)

@app.route('/categories/<int:category_id>/item/new', methods=['GET', 'POST'])
def addItem(category_id):
    '''
    Add the items and redirect the url to Home page
    :param:takes no argument
    :return: returns the added item on the Home Page
    '''
    global session
    if request.method == 'POST':
        newItem = Items(name=request.form['name'],
        description=request.form['description'],
        category_id=category_id,
        category_name= reuest.form['category'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('showcategoryItems'), category_id=category_id)
    else:
        return render_template('addnewItem.html', category_id=category_id)


@app.route('/categories/<category_name>/item_name')
def showitemDescription(category_name):
    return 'Description'.format(category_name, item_name)


@app.route('/categories/<category_name>/<item_name>/edit',
            methods=['GET', 'POST'])
def editcategoryitems(item_id):
    '''
    Edits the category items and
    :param: takes
    :return: update the item name
    '''
    return "edit the categoryitem {}".format(item_name)

@app.route('/categories/<category_name>/<item_name>/delete')
def deletecategoryitems(item_id):
    '''
    Delete the item from the category_id'''
    return "Delete the category items"



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port = 5000)
