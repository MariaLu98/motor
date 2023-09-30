import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the motor control
IN1 = 17
IN2 = 18
IN3 = 22
IN4 = 23

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the GPIO pins as output
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Define the sequence of steps for the stepper motor
# You can customize this sequence for your specific motor
# For a 4-phase stepper motor, you'll typically have 8 steps in the sequence
# The sequence should be defined based on the motor's datasheet
# This is just a sample sequence.
seq = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# Define the delay between steps (controls motor speed)
delay = 0.01

# Function to move the motor forward
def forward(steps):
    for _ in range(steps):
        for i in range(8):
            for pin in range(4):
                GPIO.output([IN1, IN2, IN3, IN4][pin], seq[i][pin])
            time.sleep(delay)

# Function to move the motor backward
def backward(steps):
    for _ in range(steps):
        for i in range(7, -1, -1):
            for pin in range(4):
                GPIO.output([IN1, IN2, IN3, IN4][pin], seq[i][pin])
            time.sleep(delay)

# Example usage:
try:
    while True:
        forward(512)  # Rotate the motor forward 512 steps
        time.sleep(1)
        backward(512) # Rotate the motor backward 512 steps
        time.sleep(1)

except KeyboardInterrupt:
    pass

# Cleanup and reset GPIO pins
GPIO.cleanup()