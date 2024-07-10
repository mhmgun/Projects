from flask import Flask, render_template_string, request   # Importing the Flask modules 
import RPi.GPIO as GPIO     # Importing the GPIO library 
from time import sleep      # Import sleep module from time library 
 servo_pin = 19 # GPIO Pin where sero is connected
GPIO.setmode(GPIO.BCM)      # Define the Pin numbering type. Here we are using BCM type
# Defing Servo Pin as output pin
GPIO.setup(servo_pin, GPIO.OUT)     
p = GPIO.PWM(servo_pin, 50)  # PWM channel at 50 Hz frequency
p.start(0) # Zero duty cycle initially
app = Flask(__name__)
#HTML Code 
TPL = '''
<html>
     <img src="https://iotdesignpro.com/sites/default/files/Iot%20Design%20Pro%20Logo_0.png" alt="">
    <head><title>Web Page Controlled Servo</title></head>
    <body>
    <h2> Web Page to Control Servo</h2>
        <form method="POST" action="test">
            <h3> Use the slider to rotate servo  </h3>
            <p>Slider   <input type="range" min="1" max="12.5" name="slider" /> </p>
            <input type="submit" value="submit" />
        </form>
    </body>
</html>

'''
@app.route("/")
def home():                                                                                                                                                         
    return render_template_string(TPL)                        
@app.route("/test", methods=["POST"])
def test():
    # Get slider Values
    slider = request.form["slider"]
    # Change duty cycle
    p.ChangeDutyCycle(float(slider))
    sleep(1)
    # Pause the servo
    p.ChangeDutyCycle(0)
    return render_template_string(TPL)
# Run the app on the local development server
if __name__ == "__main__":
    app.run()