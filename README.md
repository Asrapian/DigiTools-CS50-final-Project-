# CS50 Final Project( Digitools )
## Video Demo:  https://www.youtube.com/watch?v=0SV0NFhHhyQ
## Description:  
### summery
This web application is a Digital box containing some digital tools that can be used for many purposes.

### Programming languages used in project:
This web includes HTML CSS and some javascript for the frontend
and in backend Python , flask , SQL have been used

### Prepration to run the web Application
Note that you may need to follow these steps if you are running the program for the first time after that you don't need to follow these steps agian
  
1. first you need to have a code editor like:Vscode
2. for one of the tools you may need to install Tesseract-ocr the exe file for windows 10 64bit is included in the project you can just install it on in this directory: project/Tesseract then you are done and ready to go if you already have Tesseract-ocr follow instruction number 3
3. if you already have Tesseract-ocr installed you need to initalize the path of tesseract.exe in Digitools.py on line 18 example : tess.pytesseract.tesseract_cmd = r"Tesseract/tesseract.exe"
4. after that you need to install the needed libraries. the name of all the libraries are available in requirements.txt you can install them all by using this command "python -m pip install -r requirements.txt"
5. after that you need to run the web application by typing "flask run" in terminal while in the same directory as the web application. That's the web application will be opened soon!
### Tools
As of now there is only five tools that are available to use you can see the tools with description bellow:
QRCODE Generator: This tool can generate qr code from every type of text but this tool is commonly used for URLs but you can use it for anytype of text you wish.
  
Password Generator: For today's digital life so many people concerned about the security of the password that they use for their online accounts so for this problem we have tool that generates passwords with random length from the select menu user can chooose what type of password they want( numeric only , numeric and alphabetical and etc).
  
Ascii art generator: this tool can be used for designing purposes the usage of the tool is very simple You just select a file from your local storage with this tool you can turn any picture into an ascii art to use it in your website or any other designing purposes.
  
URL Shortener: URL shorteners are really common in today's digital life and can be used for so many purposses. There is an url shortener tool here that you can use. This url shrotener uses tinyurl host to shorten URLs.
  
Image to text:This tool allows user to extract text from any image that contain text. This is accurate for small amount of text and can't be used for a large text.

### files
Digitools.py : This file contains the python code for every tool. This file is used in app.py as a module to apply the tools based on user's input.
  
app.py : This file contains the main code for the flask web application when the website runs this code will run and will take help from Digitools module to apply the tools on the user's input.

### Main Focus
1. The main focus for making this project was to make something quite usefull that has all the Digital tools in one place (One website) with a fairly user friendly interface Sure this project is not That comeplete to have all the digital tools on earth but it is a Step to the right direction for making it happen. for user interface we really took inspiration From today's smartphones becasue they made to be quite user friendly so we did that so anybody from any age can use this website as long as they can type the website's URL ;) .

2. Our focus wasn't only on user friendliness we tried to write the code in a way that other developers can easily understand the code. for this purpose we tried to follow PEP8 Standards on writting a good style code so it will be readable.  also because of the sepration the code for tools from the main web application code The new tools can be developed easily in Digitools python file and be used in app.py by making another route and just using the function from Digitools to apply the tool on user's output That's it!

3. This project is completely Open-Source So Manhy talented Developer can add Their own tools to this web application and expand it even further!
  
### Potentials
There is so many potentials in this simple concept because as more complete Digitools gets more usefull it will be and You don't need a seprate website for each tool all of them are available in one place for free Even in furthur development of the web Application Developers can sign in and deploy their own tools and earn a passive income from this website but the website stays completely free and developers can earn income from add revenue and so many other ideas!! The said things are still concepts and the potentials the  web application as of now is a simple tools box with 5 tools that anybody can use for free.
  
### Final words
This web application actually started really small by featuring only one tool and we added more tools as the time went by we hope that this would not the end of this project but only the Beginning of something new!
 
This was our final Project Digitools
and This was cs50!

  
  
