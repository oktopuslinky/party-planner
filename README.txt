# party-planner
It allows people to plan parties.

SETUP:
  1. Install python onto your computer, and make sure to add it to your PATH while installing (the installer will tell you to do so)
  
  2. Go to command line, and type (DIR is the directory on your computer that the folder is located in):
  
    cd DIR
  
  3. Paste the following lines of code into the command line:
  
    pip install virtualenv
    pip install virtualenvwrapper-win
    mkvirtualenv venv
    setprojectdir .
    pip install flask
    python sql.py
    
*YOU CAN NOW SAFELY EXIT OUT OF THE COMMAND LINE*

TO USE APP:
  1. Go to command line, and type:
  
    workon venv
    python app.py
  
  2. Copy the URL obtained from the command line and paste that into a web browser, and ENJOY!
