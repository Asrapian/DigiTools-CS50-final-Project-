from Digitools import *
from flask import Flask , redirect, render_template, request, flash
import os
import requests
from cs50 import SQL
# generating secret key
random_string = os.urandom(12).hex() 
app=Flask(__name__)

# database configuration
db = SQL("sqlite:///feedback.db")

# configuring secret key
app.config['SECRET_KEY'] = random_string

# auto reloads templates
app.config["TEMPLATES_AUTO_RELOAD"] = True
# allowed file formats for uploads
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

# index route redirects to welcome page
@app.route("/")
def index():
    return redirect("/welcome")

# Loads the Welcome page
@app.route("/welcome")
def welcome():
   return render_template("welcome.html")

# A page that shows all the tools that are available to the user
@app.route("/tools")
def tools():
    return render_template("tools.html")

# QRcode generator tool
@app.route("/qr" , methods=[ "GET","POST"])
def qr():
    
    # if qr code file already exist delete it from the storage
    if os.path.exists("static/qr.jpg"):
        os.remove("static/qr.jpg")

    # load the webpage if request is get
    if request.method == "GET":
        return render_template("qrform.html")
    else:
        # get the user input
        url = request.form.get("url")

        # flash an error if nothing was entered
        if not url:
           flash("You need to input an Url or something to generate the QRcode")
           return redirect(request.url)

        # generate qrcode
        try:
            qr_code(url)
        except:
            flash("There was an error while trying to generate the qrcode please try again")    
        # returns the result
        return render_template("qr.html")  

# password generator
@app.route("/pass" , methods = ["GET" , "POST"])
def password():
    
    # making a list of all the options
    types = [
        "Numeric" ,"Alphabetical",
         "Numeric and Alphabetical"
    , "Numeric and Punctuation" ,
     "Alphabetical and Punctuation" 
    , "All"]
    
    # if request is post
    if request.method == "POST":
        type = request.form.get("password")

        # setting a error msg so if no options were selected this error will be displayed instead of actual password
        password = "You should Select The type of Password before generating"
        
        # generate only numeric password
        if type == types[0]:
            password = passgeneratornum()
        
        # generates only alphabetical password 
        elif type == types[1]:
            password = passgeneratoralpha()
        
        # generates a password containing alphabetial and numeric characters
        elif type == types[2]:
            password = passgeneratoralpha_num()
        
        # generates a password containing numeric and punctuation characters
        elif type == types[3]:
            password = passgeneratornum_pun()

        # generates a password containing alphabetical and punctuation characters
        elif type ==  types[4]:
            password = passgeneratoralpha_pun()  

        # generates a password containing all kinds of characters
        elif type == types[5]:
            password = passgenerator()

        return render_template("passform.html", password=password , types=types)               

    return render_template("passform.html" , types=types)         
           

def allowed_file(filename):
    """Checks to see if the file is allowed to be taken as input or not
    checks the file with ALLOWED_EXTENSIONS list"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# image to Text Converter
@app.route("/imgtotxt" , methods=["POST" , "GET"])

def imgtotxt():
    if request.method == "POST":
        # checks to see if the text file containing the extraxted text already exists if it exists deletes from the storage
        if os.path.exists("static/text.txt"):
            os.remove("static/text.txt")
        # checing to see if a file was uploaded
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)    
        
        # getting the file from request
        file = request.files['file']
        
        # double checking to see if a file was uploaded with a valid name
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # checking to see if this file type is allowed to be uploaded 
        elif not allowed_file(file.filename):
            flash("Your file extensions should be one of these : jpg , png , jpeg")
            return redirect(request.url)
        
        # declaring a variable fo the file's name
        name = file.filename

        # gets the file's format by string slicing the name
        format = name.split(".")[-1]
        
        # saving the file in determined path
        file.save(os.path.join("static/uploads/"+ "pic" + "." + format))
        image_path = "static/uploads/" + "pic" + "." + format

        # extracting the text out of the image(For more information about the function check out Digitools module)
        try:    
            text = img_to_text(image_path)
        except :
            flash("There was an error while trying to extract the text please try again later.")

        # saves the output in a txt file
        with open ("static/text.txt" , "w") as file:
            file.write(text)

        # showing the result to the user
        return render_template("imgtotext_result.html")
        
          
    return render_template("imgtotxt.html")

# url validator
def url_validator(url:str) -> bool:
    """ Cheks to see if an url is valid or not"""
    try:
        response = requests.get(url)
        return True
    except:
        return False

# url shortener
@app.route("/urlshortener", methods = ["POST" , "GET"])

def shortener():
    if request.method == "POST":
        
        url = request.form.get("url")
        # checking to see if user inputed an url
        if not url:
            flash("You didn't enter an url")
            return redirect(request.url)
        # checking to see if the url is valid
        elif url_validator(url) == False:
            flash("The url is not valid")
            return redirect(request.url)
        # shortens the url by using url_shortener function    
        shortened = url_shortener(url)
        return render_template("urlshortener.html" , shortened=shortened)    
                
    else:
        return render_template("urlshortener.html")    

# ascii art Generator
@app.route("/ascii" , methods=["GET" , "POST"])
def ascii():
    if request.method == "POST":
        # deletes the generated ascii art if it already exists
        if os.path.exists("static/ascii_art.txt"):
            os.remove("static/ascii_art.txt")
        file = request.files['file']
        # checks to see if a file was inputed
        if not file:
            flash("You need to Select a file!")
            return redirect(request.url)
        name = file.filename
        # checks to see if a file was inputed with a valid name
        if name == "" :
            flash("You need to select a file!") 
            return redirect(request.url)
        # checks to see the file that is inputed is valid    
        if not allowed_file(file.filename):
            flash("Your file extension should be one of these : jpg , png , jpeg")
            return redirect(request.url)
        # saving the format(file_extension) into a variable
        format = name.split(".")[-1]
        # saving the file
        file.save(os.path.join("static/uploads/"+ "ascii" + "." + format))
        # making the path
        image_path = "static/uploads/" + "ascii" + "." + format
        # generating the ascii art
        try:
            ascii_art = ascii_art_generator(image_path)
        except:
            flash("There was an error while trying to generate the ascii art please try again later.")
        # writting the ascii art as a tt file
        with open ("static/ascii_art.txt" , "w") as file:
            file.write(ascii_art)
        return render_template("ascii_result.html")


    return render_template("ascii.html")

# contact us page
@app.route("/contactus" , methods=["POST" , "GET"])
def contact_us():
    if request.method =="POST":
        # gets name
        name =request.form.get("name")
        
        # gets the email
        email=request.form.get("email")
        
        # gets the title
        title = request.form.get("title")
        
        # gets the selected topic option
        topic = request.form.get("topic")

        # gets the description
        description = request.form.get("description")
        
        # error checks:
        e = 0
        # if the name slot is empty
        if not name:
            flash("Name slot is empty")
            e+=1
        # if name length is valid
        if len(name) >15:
            flash("Name slot's maximum capacity is 15 characters")
            e+=1
         # if the name slot is empty   
        if not email:
            flash("Email slot is empty")
            e+=1 
        # if email length is valid
        if len(email) >50:
            flash("Email slot's maximum capacity is 50 characters")
            e+=1
        # if the title slot is empty
        if not title:
            e+=1 
        # if the title length is valid
        if len(title) >25:
            flash("Title slot's maximum capacity is 25 characters")
            e+=1
        # if description slot is empty
        if not description:
            flash("Description slot is empty")
            e+=1
        # if description is valid
        if len(description) >254:
            flash("Description slot's maximum capacity is 254 characters")
            e+=1
        # if topic is empty
        if not topic:
            flash("You need to set a topic for submitting your feedback!")
            e+=1

        if e>0:
            return redirect(request.url)
        # inserting the feedback information into feedback table if the topic is feedback
        if topic == "feedback":
            try:
                db.execute("INSERT INTO feedback (name, email, title, description) VALUES (?, ?, ?, ?)" , name , email, title, description)
                # shows the thank you image if the data insertion is succesful
                return render_template("contactus.html" , msg ="Thank you for your valuable feedback we will read it as soon as possible.")           
            except:
                flash("There was an error while trying to submit the feed back plz try again.")     
        # inserting the feedback into suggestions table if the topic is newtools
        if topic == "newtools":
            try:
                db.execute("INSERT INTO suggestions (name, email, title, description) VALUES (?, ?, ?, ?)" , name , email, title, description)
                # shows the thank you image if the data insertion is succesful
                return render_template("contactus.html" , msg ="Thank you for helping us expand our simple website by recommanding new tools to add, we will read it as soon as possible or contact you further if needed.")             
            except:
                flash("There was an error while trying to submit the feed back plz try again.") 

    return render_template("contactus.html")

# debugger is on while running
if __name__ == '__main__':
    app.run(debug=True)


