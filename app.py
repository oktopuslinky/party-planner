#!/usr/bin/python

#Imports flask, render_template
from flask import Flask, render_template, redirect, url_for, request, session, flash, g, jsonify
from functools import wraps
import sqlite3, cgi, cgitb, json

cgitb.enable()
#create the application object
app=Flask(__name__)

#attach the database to the application
app.database='sample.db'
'''
Things to note about secret keys:
    • You need a secret key for sessions to work properly
    • The session key protects the session from being accessed through the client side
'''
app.secret_key = "my precious"

#create a function that will connect to our database, 
#and create a database object that we can interact with.
def connect_db():
    return sqlite3.connect(app.database)
    
#Use a decorator to join url to function
@app.route('/')
#@login_required

def home():
    return render_template('categories.html')

@app.route('/ambience')
def ambience():
    g.db = connect_db()
    #query the database
    cur = g.db.execute("SELECT * FROM ambience")
    posts=[dict(id=row[0], checked=row[1], inputVal=row[2]) for row in cur.fetchall()]
    print(posts)
    #print(posts)
    return render_template('ambience.html', posts=posts)
    g.db.close()

@app.route('/processAmbience', methods=['POST'])
def processAmbience():
    if request.method=="POST":
        #light=request.form["Lighting"]
        #print(light)
        print('POSTED')
        
        lightingData=request.form['lighting']
        decorationsData=request.form['decorations']
        musicData=request.form['music']
        entertainmentData=request.form['entertainment']


        lightingTextData=request.form['lightingText']
        decorationsTextData=request.form['decorationsText']
        musicTextData=request.form['musicText']
        entertainmentTextData=request.form['entertainmentText']

        print(lightingData)
        print(decorationsData)

        print(lightingTextData)
        print(decorationsTextData)

        g.db = connect_db()
        #update each of the values
        cur=g.db.cursor()

        cur.execute("UPDATE ambience SET checked=?, inputVal=? WHERE id='Lighting';", [lightingData, lightingTextData])
        cur.execute("UPDATE ambience SET checked=?, inputVal=? WHERE id='Decorations';", [decorationsData, decorationsTextData])
        cur.execute("UPDATE ambience SET checked=?, inputVal=? WHERE id='Music';", [musicData, musicTextData])
        cur.execute("UPDATE ambience SET checked=?, inputVal=? WHERE id='Entertainment';", [entertainmentData, entertainmentTextData])

        g.db.commit()
        cur2=cur.execute('SELECT * FROM ambience')
        print(cur2.fetchall())
        return render_template('categories.html')

@app.route('/foodAndDrinks')
def foodAndDrinks():
    g.db = connect_db()
    cur = g.db.execute("SELECT * FROM foodAndDrinks")
    posts=[dict(id=row[0], checked=row[1], inputVal=row[2]) for row in cur.fetchall()]
    print(posts)
    return render_template('foodAndDrinks.html', posts=posts)

@app.route('/processFoodAndDrinks', methods=['POST'])
def processFoodAndDrinks():
    if request.method=="POST":
        #light=request.form["Lighting"]
        #print(light)
        print('POSTED')
        
        appetizersData=request.form['appetizers']
        mainEntreesData=request.form['mainEntrees']
        dessertsData=request.form['desserts']
        snacksData=request.form['snacks']
        drinksData=request.form['drinks']
        forksData=request.form['forks']
        knivesData=request.form['knives']
        spoonsData=request.form['spoons']
        platesData=request.form['plates']
        bowlsData=request.form['bowls']
        cupsData=request.form['cups']
        napkinsData=request.form['napkins']

        appetizersTextData=request.form['appetizersText']
        mainEntreesTextData=request.form['mainEntreesText']
        dessertsTextData=request.form['dessertsText']
        snacksTextData=request.form['snacksText']
        drinksTextData=request.form['drinksText']
        forksTextData=request.form['forksText']
        knivesTextData=request.form['knivesText']
        spoonsTextData=request.form['spoonsText']
        platesTextData=request.form['platesText']
        bowlsTextData=request.form['bowlsText']
        cupsTextData=request.form['cupsText']
        napkinsTextData=request.form['napkinsText']

        g.db = connect_db()
        #update each of the values
        cur=g.db.cursor()

        cur.execute("UPDATE foodAndDrinks SET checked=?, inputVal=? WHERE id='Appetizers';", [appetizersData, appetizersTextData])
        cur.execute("UPDATE foodAndDrinks SET checked=?, inputVal=? WHERE id='MainEntrees';", [mainEntreesData, mainEntreesTextData])
        cur.execute("UPDATE foodAndDrinks SET checked=?, inputVal=? WHERE id='Desserts';", [dessertsData, dessertsTextData])
        cur.execute("UPDATE foodAndDrinks SET checked=?, inputVal=? WHERE id='Snacks';", [snacksData, snacksTextData])
        cur.execute("UPDATE foodAndDrinks SET checked=?, inputVal=? WHERE id='Drinks';", [drinksData, drinksTextData])
        cur.execute("UPDATE foodAndDrinks SET checked=?, inputVal=? WHERE id='Forks';", [forksData, forksTextData])
        cur.execute("UPDATE foodAndDrinks SET checked=?, inputVal=? WHERE id='Knives';", [knivesData, knivesTextData])
        cur.execute("UPDATE foodAndDrinks SET checked=?, inputVal=? WHERE id='Spoons';", [spoonsData, spoonsTextData])
        cur.execute("UPDATE foodAndDrinks SET checked=?, inputVal=? WHERE id='Plates';", [platesData, platesTextData])
        cur.execute("UPDATE foodAndDrinks SET checked=?, inputVal=? WHERE id='Bowls';", [bowlsData, bowlsTextData])
        cur.execute("UPDATE foodAndDrinks SET checked=?, inputVal=? WHERE id='Cups';", [cupsData, cupsTextData])
        cur.execute("UPDATE foodAndDrinks SET checked=?, inputVal=? WHERE id='Napkins';", [napkinsData, napkinsTextData])

        g.db.commit()
        cur2=cur.execute('SELECT * FROM foodAndDrinks')
        print(cur2.fetchall())
        return render_template('categories.html')

@app.route('/back')
def back():
    return render_template('categories.html')

@app.route('/guests')
def guests():
    g.db = connect_db()
    cur = g.db.execute("SELECT * FROM guests")
    posts=[dict(id=row[0], checked=row[1], inputVal=row[2]) for row in cur.fetchall()]
    print(posts)
    return render_template('guests.html', posts=posts)

@app.route('/processGuests', methods = ['POST'])
def processGuests():
    if request.method=="POST":
        #light=request.form["Lighting"]
        #print(light)
        print('POSTED')
        
        guestListData=request.form['guestList']
        volunteerSignupData=request.form['volunteerSignup']
        eventInfoData=request.form['eventInfo']

        guestListTextData=request.form['guestListText']
        volunteerSignupTextData=request.form['volunteerSignupText']
        eventInfoTextData=request.form['eventInfoText']

        g.db = connect_db()
        #update each of the values
        cur=g.db.cursor()

        cur.execute("UPDATE guests SET checked=?, inputVal=? WHERE id='GuestList';", [guestListData, guestListTextData])
        cur.execute("UPDATE guests SET checked=?, inputVal=? WHERE id='VolunteerSignup';", [volunteerSignupData, volunteerSignupTextData])
        cur.execute("UPDATE guests SET checked=?, inputVal=? WHERE id='EventInfo';", [eventInfoData, eventInfoTextData])

        g.db.commit()
        cur2=cur.execute('SELECT * FROM guests')
        print(cur2.fetchall())
        return render_template('categories.html')

#Start server with run method
if __name__ == '__main__':
    app.run(debug=True)
