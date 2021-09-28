# CS50 Final Project( Digitools )
## Video Demo:  <URL HERE>
## Description:  
### summery
This web application is a Digital box containing some digital tools that can be used for many purposes.

### Programming languages used in project:
This web includes HTML CSS and some javascript for the front end
and in back end Python , flask , SQL have been used

### Prepration to run the web Application
1. first you need to have a code editor like:Vscode
2. for one of the tools you may need to install Tesseract-ocr the exe file for windows 10 64bit is included in the project you can just install it on in this directory: project/Tesseract then you are done and ready to go if you already have Tesseract-ocr follow instruction number 3
3. if you already have Tesseract-ocr installed you need to initalize the path of tesseract.exe in Digitools.py on line 18 example : tess.pytesseract.tesseract_cmd = r"Tesseract/tesseract.exe"
4. after that you need to install the needed libraries. the name of all the libraries are available in requirements.txt you can install them all by using this command "python -m pip install -r requirements.txt"
5. after that you need to run the web application by typing "flask run" in terminal while in the same directory as the web application. That's the web application will be opened soon!
### Tools
As of now there is only five tools that are available to use you can see the tools with description bellow:
