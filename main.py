import RPi.GPIO as GPIO
import time

# Set GPIO pin numbers
TRIG_PIN = 17
ECHO_PIN = 18

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up TRIG_PIN as an output and ECHO_PIN as an input
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

try:
    while True:
        # Send a 10us pulse to trigger the sensor
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)

        while GPIO.input(ECHO_PIN) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO_PIN) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150  # Speed of sound in cm/s

        print(f"Distance: {distance:.2f} cm")
        time.sleep(1)  # Delay between readings

except KeyboardInterrupt:
    GPIO.cleanup()  # Cleanup GPIO on Ctrl+C exit

GPIO.cleanup()  # Cleanup GPIO on normal exit