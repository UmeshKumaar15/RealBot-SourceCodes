# import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__, template_folder = 'template')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

forward= 2
left= 3
right = 4
reverse = 14 

fs = 0
ls = 0
rs = 0
res = 0
s =  0

GPIO.setup(forward, GPIO.OUT)
GPIO.setup(left,GPIO.OUT)
GPIO.setup(right, GPIO.OUT)
GPIO.setup(reverse, GPIO.OUT)

GPIO.output(forward, GPIO.LOW)
GPIO.output(left, GPIO.LOW)
GPIO.output(right, GPIO.LOW)
GPIO.output(reverse, GPIO.LOW)

@app.route('/')
def index():
    fs = GPIO.input(forward)
    ls = GPIO.input(left)
    rs = GPIO.input(right)
    res = GPIO.input(reverse)
   
    templateData = { 'forward' : fs,
    'left' : ls,
    'right' : rs,
    'reverse' : res,
    'stop' : s }
   
    return render_template('carpage.html', **templateData)

@app.route('/<button>')
def do(button):
    if button == "forward":
        GPIO.output(forward, GPIO.HIGH)
        GPIO.output(right, GPIO.HIGH)

    if button == "left":
        GPIO.output(forward, GPIO.HIGH)
        GPIO.output(right, GPIO.LOW)

    if button == "right":
        GPIO.output(right, GPIO.HIGH)
        GPIO.output(forward, GPIO.LOW)

    if button == "reverse":
        GPIO.output(left, GPIO.HIGH)
        GPIO.output(reverse, GPIO.HIGH)

    if button == "stop":
        GPIO.output(forward, GPIO.LOW)
        GPIO.output(left, GPIO.LOW)
        GPIO.output(right, GPIO.LOW)
        GPIO.output(reverse, GPIO.LOW)
       

    fs = GPIO.input(forward)
    ls = GPIO.input(left)
    rs = GPIO.input(right)
    res = GPIO.input(reverse)
   
    templateData = { 'forward' : fs,
    'left' : ls,
    'right' : rs,
    'reverse' : res,
    'stop' : s }

    return render_template('carpage.html', **templateData )

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)