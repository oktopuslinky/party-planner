#!/usr/bin/python

'''

TO DO:
(WORK OUT THE CHECKED STATE IN EACH OF THE INPUT CHECKBOXES, TO DISPLAY THE CORRECT ONE BASED ON DATABASE)

• apply ambience code to all 4 pages



'''


#Imports flask, render_template
from flask import Flask, render_template, redirect, url_for, request, session, flash, g, jsonify
from functools import wraps
import sqlite3, cgi, cgitb, json, requests

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

'''
#login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''

#create a function that will connect to our database, 
#and create a database object that we can interact with.
def connect_db():
    return sqlite3.connect(app.database)
    
#Use a decorator to join url to function
@app.route('/')
#@login_required

def home():
    return render_template('categories.html')
    """
    '''
    Purpose: Direct the user to the home page, which is the page with the list of parties.
    Post-condition:
    '''
    #start by establishing the connection.
    #We are going to use an object called g.
    #g is an object specific to flask, that's used to store a temporary object during a request.
    
    g.db = connect_db()
    #query the database
    cur = g.db.execute("SELECT * FROM ambience")
    #When fetching the data from the posts table, we want to cast it to a dictionary.
    posts=[dict(id=row[0], checked=row[1], desc=row[2]) for row in cur.fetchall()]
    #close the database
    g.db.close()

    return render_template('partiesList.html')


    '''
    #pass the posts variable to the template
    return render_template('welcome.html', posts=posts)'''
    """
'''
add another route
note: the text in the app.route parentheses must be exactly the same 
as the file you want to open.
'''


'''
adds route to the login page, 
and defines the methods used.

we need the '['GET', 'POST']', 
because by default, the method is GET, 
and to apply another method, it needs to be defined.
'''
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None

    #handles POST method
    if request.method=='POST':
        #if credentials are invalid
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials, please try again.'
        #if credentials are valid, redirect the user to home.
        else:
            #If the user's credentials are correct, 
            #the value 'True' is assigned to key 'logged_in'
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('ambience'))
    return render_template("login.html", error=error)

#When a GET request is sent to the logout route, 
#we pop out the value of True out of the session object and replace it with None,
#and this deletes the key.
@app.route('/logout')
@login_required

def logout():
    session.pop('logged_in', None)
    #Then, redirect the user to the partiesList page.

    flash('You were just logged out!')
    return redirect(url_for('login'))
'''
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

'''
@app.route('/categories')
def categories():
    return render_template('categories.html')
'''

'''
@app.route('/postmethod', methods=['POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    newJs=json.loads(jsdata)[0]
    print(newJs)
    return jsdata
'''

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
'''
@app.route('/backup')
def backup():
    g.db = connect_db()
    cur = g.db.execute("SELECT * FROM backup")
    posts=[dict(id=row[0], checked=row[1]) for row in cur.fetchall()]
    print(posts)
    return render_template('backup.html', posts=posts)

@app.route('/processBackup')
def processBackup():
    if request.method=="POST":
        print('POSTED')

        sterileGauzePadsData=request.form['sterileGauzePads']
        adhesiveTapeData=request.form['adhesiveTape']
        bandAidsData=request.form['bandAids']
        examGlovesData=request.form['examGloves']
        antisepticPadsData=request.form['antisepticPads']
        tweezersData=request.form['tweezers']
        icePacksData=request.form['icePacks']
        itchCreamData=request.form['itchCream']
        antibioticCreamData=request.form['antibioticCream']
        digitalThermometerData=request.form['digitalThermometer']
        towelsData=request.form['towels']
        mopData=request.form['mop']
        broomData=request.form['broom']
        trashCanData=request.form['trashCan']
        sprayBottleData=request.form['sprayBottle']

        g.db = connect_db()
        #update each of the values
        cur=g.db.cursor()

        cur.execute("UPDATE backup SET checked=? WHERE id='SterileGauzePads';", [sterileGauzePadsData])
        cur.execute("UPDATE backup SET checked=? WHERE id='AdhesiveTape';", [adhesiveTapeData])
        cur.execute("UPDATE backup SET checked=? WHERE id='BandAids';", [bandAidsData])
        cur.execute("UPDATE backup SET checked=? WHERE id='ExamGloves';", [examGlovesData])
        cur.execute("UPDATE backup SET checked=? WHERE id='AntisepticPads';", [antisepticPadsData])
        cur.execute("UPDATE backup SET checked=? WHERE id='Tweezers';", [tweezersData])
        cur.execute("UPDATE backup SET checked=? WHERE id='IcePacks';", [icePacksData])
        cur.execute("UPDATE backup SET checked=? WHERE id='ItchCream';", [itchCreamData])
        cur.execute("UPDATE backup SET checked=? WHERE id='AntibioticCream';", [antibioticCreamData])
        cur.execute("UPDATE backup SET checked=? WHERE id='DigitalThermometer';", [digitalThermometerData])
        cur.execute("UPDATE backup SET checked=? WHERE id='Towels';", [towelsData])
        cur.execute("UPDATE backup SET checked=? WHERE id='Mop';", [mopData])
        cur.execute("UPDATE backup SET checked=? WHERE id='Broom';", [broomData])
        cur.execute("UPDATE backup SET checked=? WHERE id='TrashCan';", [trashCanData])
        cur.execute("UPDATE backup SET checked=? WHERE id='SprayBottle';", [sprayBottleData])

        g.db.commit()
        cur2=cur.execute('SELECT * FROM backup')
        print(cur2.fetchall())
        return render_template('categories.html')
'''
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
'''
@app.route('/backup')
def backup():
    g.db = connect_db()
    cur = g.db.execute("SELECT * FROM backup")
    posts=[dict(id=row[0], checked=row[1], inputVal=row[2]) for row in cur.fetchall()]
    print(posts)
    return render_template('backup.html', posts=posts)
'''
#Start server with run method
if __name__ == '__main__':
    app.run(debug=True)
