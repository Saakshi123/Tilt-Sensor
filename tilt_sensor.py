import RPi.GPIO as GPIO
import time
import lcddriver
import requests
 
 
display = lcddriver.lcd()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.OUT)
 
 
url = "https://api.ciscospark.com/v1/messages"
 
payload = "roomId=Y2lzY29zcGFyazovL3VzL1JPT00vMjAyZWVmZDAtMDJmOS0xMWU5LWEyZWYtYzU3MmNjMzA2YWMx&text=TILTED!&undefined="
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Authorization': "Bearer MDUwMDU2MjYtZmUyNy00NjQzLWEzOGItOWZhN2JlZjU5MWQwOTE2NDQ0ZDUtMDVl_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
    'cache-control': "no-cache",
    'Postman-Token': "4c5b1d6a-8a94-4267-bc3d-e364b17c3145"
    }
 
print "Tilt Sensor Demo begins" 
 
# This output function will be started at signal detection
def outFunction(null):
    print("Signal detected")
 
    display.lcd_display_string("Tilt Detected!", 1) # Write line of text to first line of display
    display.lcd_display_string("watch out!", 2) # Write line of text to second line of display
 
    time.sleep(2)
    display.lcd_clear() # clear lcd display screen
    GPIO.output(26, GPIO.HIGH) # GPIO Pin 26 to glow-high
    time.sleep(1) # for blink effect
    GPIO.output(26, GPIO.LOW) # GPIO Pin 26 to glow-low
    time.sleep(1)
    
    GPIO.output(26, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(26, GPIO.LOW)
    time.sleep(1)
    response = requests.request("POST", url, data=payload, headers=headers)
    #print(response.text)
    
    

# The output function will be activated after a signal was detected.
GPIO.add_event_detect(19, GPIO.FALLING, callback=outFunction, bouncetime=100) 
 
# main program loop 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    GPIO.cleanup()
 

