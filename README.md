# GreenCanThingy

## Overview

We will use an ultrasound sensor to detect how far the XXL can has been filled. This data will then be send to a database, from where on the data can be used as whished.

## Components Needed

- Raspberry Pi (any model with GPIO pins will work)
- Ultrasonic sensor (e.g., HC-SR04)
- Breadboard and jumper wires
- Power source for the Raspberry Pi

## Project Setup

### 1. Connecting the Ultrasonic Sensor

- Connect the VCC pin of the sensor to the 5V pin on the Raspberry Pi.
- Connect the GND pin of the sensor to a ground (GND) pin on the Raspberry Pi.
- Connect the TRIG pin of the sensor to a GPIO pin (e.g., GPIO17).
- Connect the ECHO pin of the sensor to another GPIO pin (e.g., GPIO18).

### 2. Writing Code

- We will use python with librarys like RPi.GPIO and gpiozero
- The script will send a signal (pulse) to the TRIG pin, wait for the ultrasound pulse to return, and calculate the distance based on the time it takes for the pulse to travel.
