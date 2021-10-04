# This Module is made for the Digitools website
# this module is made for none commercial purposes This module was mainly made for CS50 Final Project
# Open-source
import string
import random
import qrcode
import os
import pyshorteners
import pytesseract as tess
from PIL import Image
# Initializing tesseract route to use it for pytesseract module
# for using img_to_text function firt you need to follow these steps

# 1.install pytesseract module
# 2.Download an executable version of tesseract by getting it from this address: https://tesseract-ocr.github.io/tessdofc/Home.html
# 3. install it in final project folder
# 4. Initialize by setting the path to the tesseract like bellow
tess.pytesseract.tesseract_cmd = r"Tesseract/tesseract.exe"
#qrcode generator
def qr_code(link:str):
    """this function takes an internet url or any other 
        type of data as an argument
        and returns the qrcode as the output."""
    # checks to if a file as qr code exists if it  exists delete it to replace it with a new one
    if os.path.exists("static/qr.jpg"):
        os.remove("static/qr.jpg")

    # generates the qrcode
    qr = qrcode.make(link)
    # doesn't return any value just saves the qr code as a jpg file
    # the jpg file should be linked into the HTML file
    qr.save("static/qr.jpg")
    
# Password generator(All)
def passgenerator()->str:
    """ a function that generates a random password between 8 to 16 characters long,
        the password includes(Alphabetical characters and numeric characters and punctuation)."""
    # setting up the characters(ALL) as password characters    
    ch = string.ascii_letters+string.digits+string.punctuation
    # choosing random from characters for a random length(between 8 , 16)
    output = "".join(random.choice(ch) for x in range(random.randint(8,16)))
    return output

# Password generator (alphabetical only)
def passgeneratoralpha()->str:
    """ a function that generates a random password between 8 to 16 characters long,
        the password includes(Alphabetical characters)."""
    # setting up alphabetical characters as password characters
    alpha = string.ascii_letters
    # choosing random from characters for a random length(between 8 , 16)
    output = "".join(random.choice(alpha) for x in range(random.randint(8,16)))
    return output

# Password generator (Numeric Only)
def passgeneratornum()->str:
    """ a function that generates a random password between 8 to 16 characters long,
        the password includes( numeric characters )."""
    # setting up numeric characters as password characters
    num = string.digits
    # choosing random from characters for a random length(between 8 , 16)
    output = "".join(random.choice(num) for x in range(random.randint(8,16)))
    return output

# Password generator (Alphabetical and numeric)
def passgeneratoralpha_num()->str:
    """ a function that generates a random password between 8 to 16 characters long,
        the password includes(Alphabetical characters and numeric characters)."""
    # setting up numeric and alphabetical characters as password characters
    ch = string.ascii_letters+string.digits
    # choosing random from characters for a random length(between 8 , 16)
    output = "".join(random.choice(ch) for x in range(random.randint(8,16)))
    return output

# Password generator (Alphabetical and Punctuation)
def passgeneratoralpha_pun()->str:
    """ a function that generates a random password between 8 to 16 characters long,
        the password includes(Alphabetical characters  and punctuation)."""
        # setting up punctuation and alphabetical characters as password characters
    ch = string.ascii_letters+string.punctuation
    # choosing random from characters for a random length(between 8 , 16)
    output = "".join(random.choice(ch) for x in range(random.randint(8,16)))
    return output

# Password generator (Numeric and Punctuation)
def passgeneratornum_pun()->str:
    """ a function that generates a random password between 8 to 16 characters long,
        the password includes( numeric characters and punctuation)."""
        # setting up punctuation and numeric characters as password characters
    ch = string.digits+string.punctuation
    # choosing random from characters for a random length(between 8 , 16)
    output = "".join(random.choice(ch) for x in range(random.randint(8,16)))
    return output

# Url shortener 
def url_shortener(url:str)->str :
    """ a function that takes an url address as an input 
    and return the shortened url as output , 
    keep that in mind for some regions you may need to use some kind of a vpn service
    for this too work"""
    shortener = pyshorteners.Shortener()
    try:
        shortened = shortener.tinyurl.short(url)
        return shortened
    except:
        shortened = "Connection Error"
              
# Image to Text converter
def img_to_text(image_path:str) -> str:
    """This Function takes an image path as an argument and extracts the text out of the
     image using tesseract and pytesseract module"""
     # This function have been made with the help of this youtube video : https://www.youtube.com/watch?v=4DrCIVS5U3Y
    text=tess.image_to_string(image_path)
    return text

def ascii_art_generator(path:str)->str:
    """This Function uses PIL module and takes an image as an input 
    and converts into an ascii art """
    # This function have been made with the help of this youtube video : https://www.youtube.com/watch?v=7SGlLwC1BXE&t=309s
    
    # opening the image 
    input = Image.open(path)
    # reading the width and height
    width , height = input.size
    # calculating ratio
    ratio = height / width
    # setting up the new width and height
    new_width = 100
    # resizing it turning the picture into black and white
    new_height = ratio * new_width * 0.55
    image = input.resize((new_width , int(new_height)))
    image = image.convert("L")
    # reading the pixels of the image
    pixels = image.getdata()
    # configuring the characters in ascii art
    characters = list("BS#&@$%*!:.")
    # turning the greyscale picture into ascii art
    n_pixels = [characters[pixel // 25]for pixel in pixels]
    n_pixels = "".join(n_pixels)
    count = len(n_pixels)
    ascii_image = [n_pixels[index:index+new_width]for index in range (0 , count , new_width)]
    ascii_art = "\n".join(ascii_image)
    return ascii_art

    
    








