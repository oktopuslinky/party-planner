import sqlite3

#Create connection to database, and creates database if it doesn't exist.
with sqlite3.connect("sample.db") as connection:
    #define a cursor, which allows us to interact with the database itself.
    c = connection.cursor()
    #create a new table
    
    """
    c.execute("CREATE TABLE ambience(id TEXT, inputVal TEXT, checked TEXT)")
    c.execute(
        '''
        INSERT INTO ambience VALUES(
            "Lighting", "", "False"
        )
        '''
    )
    c.execute(
        '''
        INSERT INTO ambience VALUES(
            "Decorations, "", "False"
        )
        '''
    )
    c.execute(
        '''
        INSERT INTO ambience VALUES(
            "Music, "", "False"
        )
        '''
    )
    c.execute(
        '''
        INSERT INTO ambience VALUES(
            "Entertainment, "", "False"
        )
        '''
    )
    """
    c.execute("DROP TABLE ambience")
    c.execute("CREATE TABLE ambience(id TEXT, checked TEXT, inputVal TEXT)")
    #Add some data
    c.execute(
        '''
        INSERT INTO ambience VALUES(
            "Lighting", "False", ""
        )
        '''
    )
    c.execute(
        '''
        INSERT INTO ambience VALUES(
            "Decorations", "False", ""
        )
        '''
    )
    c.execute(
        '''
        INSERT INTO ambience VALUES(
            "Music", "False", ""
        )
        '''
    )
    c.execute(
        '''
        INSERT INTO ambience VALUES(
            "Entertainment", "False", ""
        )
        '''
    )

    """
    c.execute("CREATE TABLE backup(id TEXT, checked TEXT, inputVal TEXT)")
    c.execute(
        '''
        INSERT INTO backup VALUES(
            ""
        )
        '''
    )
    """

    c.execute("DROP TABLE foodAndDrinks")
    c.execute("CREATE TABLE foodAndDrinks(id TEXT, checked TEXT, inputVal TEXT)")
    c.execute('INSERT INTO foodAndDrinks VALUES("Appetizers", "False", "")')
    c.execute('INSERT INTO foodAndDrinks VALUES("MainEntrees", "False", "")')
    c.execute('INSERT INTO foodAndDrinks VALUES("Desserts", "False", "")')
    c.execute('INSERT INTO foodAndDrinks VALUES("Snacks", "False", "")')
    c.execute('INSERT INTO foodAndDrinks VALUES("Drinks", "False", "")')
    c.execute('INSERT INTO foodAndDrinks VALUES("Forks", "False", "")')
    c.execute('INSERT INTO foodAndDrinks VALUES("Knives", "False", "")')
    c.execute('INSERT INTO foodAndDrinks VALUES("Spoons", "False", "")')
    c.execute('INSERT INTO foodAndDrinks VALUES("Plates", "False", "")')
    c.execute('INSERT INTO foodAndDrinks VALUES("Bowls", "False", "")')
    c.execute('INSERT INTO foodAndDrinks VALUES("Cups", "False", "")')
    c.execute('INSERT INTO foodAndDrinks VALUES("Napkins", "False", "")')

    c.execute("DROP TABLE guests")
    c.execute("CREATE TABLE guests(id TEXT, checked TEXT, inputVal TEXT)")
    c.execute('INSERT INTO guests VALUES("GuestList", "False", "")')
    c.execute('INSERT INTO guests VALUES("VolunteerSignup", "False", "")')
    c.execute('INSERT INTO guests VALUES("EventInfo", "False", "")')

    c.execute("DROP TABLE backup")
    c.execute("CREATE TABLE backup(id TEXT, checked TEXT)")
    c.execute('INSERT INTO backup VALUES("SterileGauzePads", "true")')
    c.execute('INSERT INTO backup VALUES("AdhesiveTape", "false")')
    c.execute('INSERT INTO backup VALUES("BandAids", "false")')
    c.execute('INSERT INTO backup VALUES("ExamGloves", "false")')
    c.execute('INSERT INTO backup VALUES("AntisepticPads", "false")')
    c.execute('INSERT INTO backup VALUES("Tweezers", "false")')
    c.execute('INSERT INTO backup VALUES("IcePacks", "false")')
    c.execute('INSERT INTO backup VALUES("ItchCream", "false")')
    c.execute('INSERT INTO backup VALUES("AntibioticCream", "false")')
    c.execute('INSERT INTO backup VALUES("DigitalThermometer", "false")')
    c.execute('INSERT INTO backup VALUES("Towels", "false")')
    c.execute('INSERT INTO backup VALUES("Mop", "false")')
    c.execute('INSERT INTO backup VALUES("Broom", "false")')
    c.execute('INSERT INTO backup VALUES("TrashCan", "false")')
    c.execute('INSERT INTO backup VALUES("SprayBottle", "false")')