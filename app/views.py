# -*- coding: utf8 -*-
from flask import render_template, redirect, url_for, abort, request,\
    current_app
from flask.ext.uuid import uuid
from . import db, app
from models import User

def get_user_by_id(id):
    return User.query.filter_by(uuid=id).first()


@app.route('/')
def index():
	return render_template('page0.html')

@app.route('/1')
def goto1():
	random_uuid=uuid.uuid4()
	url=url_for('page1',id=random_uuid)
	return redirect(url)

@app.route('/<uuid:id>/')
def page0(id):
    return render_template('page0.html')

@app.route('/<uuid:id>/1', methods=['GET', 'POST'])
def page1(id):
    if request.method == 'POST':
        user = get_user_by_id(id.hex)
        if user is not None:
            user.sex = request.form['sex']
            db.session.commit()
        else:    
            user = User(id.hex)
            user.sex = request.form['sex']
            db.session.add(user)
            db.session.commit()

        if user.sex == False:
            next_page = 'page2'
        else:
            next_page = 'page6'
        url = url_for(next_page, id=id)
        return redirect(url)
    return render_template('page1.html')

@app.route('/<uuid:id>/2', methods=['GET', 'POST'])
def page2(id):
    if request.method == 'POST':
        user = get_user_by_id(id.hex)
        if user is not None:
            user.character = request.form['character']
            db.session.commit()
        else:    
            user = User(id.hex)
            user.character = request.form['character']
            db.session.add(user)
            db.session.commit()

        if user.sex is None:
            next_page = 'page1'
        elif user.sex == False:
            next_page = 'page3'
        else:
            next_page = 'page7'
        url = url_for(next_page, id=id)
        return redirect(url)
    return render_template('page2.html')

@app.route('/<uuid:id>/6', methods=['GET', 'POST'])
def page6(id):
    if request.method == 'POST':
        user = get_user_by_id(id.hex)
        if user is not None:
            user.character = request.form['character']
            db.session.commit()
        else:    
            user = User(id.hex)
            user.character = request.form['character']
            db.session.add(user)
            db.session.commit()
        if user.sex is None:
            next_page = 'page1'
        elif user.sex == False:
            next_page = 'page3'
        else:
            next_page = 'page7'
        url = url_for(next_page, id=id)
        return redirect(url)
    return render_template('page6.html')


@app.route('/<uuid:id>/3', methods=['GET', 'POST'])
def page3(id):
    if request.method == 'POST':
        user = get_user_by_id(id.hex)
        if user is not None:
            user.nickname = request.form['nickname']
            db.session.commit()
        else:    
            user = User(id.hex)
            user.nickname = request.form['nickname']
            db.session.add(user)
            db.session.commit()
        if user.sex is None:
            next_page = 'page1'
        elif user.sex == False:
            next_page = 'page4'
        else:
            next_page = 'page8'
        url = url_for(next_page, id=id)
        return redirect(url)
    return render_template('page3.html')

@app.route('/<uuid:id>/7', methods=['GET', 'POST'])
def page7(id):
    if request.method == 'POST':
        user = get_user_by_id(id.hex)
        if user is not None:
            user.nickname = request.form['nickname']
            db.session.commit()
        else:    
            user = User(id.hex)
            user.nickname = request.form['nickname']
            db.session.add(user)
            db.session.commit()

        if user.sex is None:
            next_page = 'page1'
        elif user.sex == False:
            next_page = 'page4'
        else:
            next_page = 'page8'
        url = url_for(next_page, id=id)
        return redirect(url)
    return render_template('page7.html')

@app.route('/<uuid:id>/4', methods=['GET', 'POST'])
def page4(id):
    if request.method == 'POST':
        user = get_user_by_id(id.hex)
        if user is not None:
            user.words = request.form['words']
            db.session.commit()
        else:    
            user = User(id.hex)
            user.words = request.form['words']
            db.session.add(user)
            db.session.commit()
        if user.sex is None:
            next_page = 'page1'
        elif user.sex == False:
            next_page = 'page5'
        else:
            next_page = 'page9'
        url = url_for(next_page, id=id)
        return redirect(url)
    return render_template('page4.html')

@app.route('/<uuid:id>/8', methods=['GET', 'POST'])
def page8(id):
    if request.method == 'POST':
        user = get_user_by_id(id.hex)
        if user is not None:
            user.words = request.form['words']
            db.session.commit()
        else:    
            user = User(id.hex)
            user.words = request.form['words']
            db.session.add(user)
            db.session.commit()
        if user.sex is None:
            next_page = 'page1'
        elif user.sex == False:
            next_page = 'page5'
        else:
            next_page = 'page9'
        url = url_for(next_page, id=id)
        return redirect(url)
    return render_template('page8.html')

@app.route('/<uuid:id>/5', methods=['GET', 'POST'])
def page5(id):
    if request.method == 'POST':
        user = get_user_by_id(id.hex)
        if user is not None:
            user.wechat = request.form['wechat']
            db.session.commit()
        else:    
            user = User(id.hex)
            user.wechat = request.form['wechat']
            db.session.add(user)
            db.session.commit()

        if user.sex is None:
            next_page = 'page1'
        elif user.character is None:
            next_page = 'page2'
        elif user.nickname is None:
            next_page = 'page3'
        elif user.words is None:
            next_page = 'page4'
        else:
            next_page = 'page10'
            user.completed = True
            db.session.commit()
        url = url_for(next_page, id=id)
        return redirect(url)
    return render_template('page5.html')

@app.route('/<uuid:id>/9', methods=['GET', 'POST'])
def page9(id):
    if request.method == 'POST':
        user = get_user_by_id(id.hex)
        if user is not None:
            user.wechat = request.form['wechat']
            db.session.commit()
        else:
            user = User(id.hex)
            user.wechat = request.form['wechat']
            db.session.add(user)
            db.session.commit()
        if user.sex is None:
            next_page = 'page1'
        elif user.character is None:
            next_page = 'page6'
        elif user.nickname is None:
            next_page = 'page7'
        elif user.words is None:
            next_page = 'page8'
        else:
            next_page = 'page10'
            user.completed = True
            db.session.commit()
        url = url_for(next_page, id=id)
        return redirect(url)
    return render_template('page9.html')

@app.route('/<uuid:id>/10')
def page10(id):
    user = get_user_by_id(id.hex)
    if user.sex is None:
        next_page = 'page1'
    elif user.character is None:
        if user.sex == True:
            next_page = 'page6'
        else:
            next_page = 'page2'
    elif user.nickname is None:
        if user.sex == True:
            next_page = 'page7'
        else:
            next_page = 'page3'
    elif user.words is None:
        if user.sex == True:
            next_page = 'page8'
        else:
            next_page = 'page4'
    elif user.wechat is None:
        if user.sex == True:
            next_page = 'page9'
        else:
            next_page = 'page5'
    else:
        return render_template('page10.html', user=user)
    url = url_for(next_page, id=id)
    return redirect(url)
    
