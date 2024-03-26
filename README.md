# Control LED & DC Motor on Raspberry Pi
A Python script to control a DC motor and LED.

## Setup
The physical setup uses a breadboard and contains 2 physical buttons, each button controlling the LED and DC motor respectively. The breadboard is connected to the Pi's GPIO pins. Adjust the setup accordingly to suit your needs.

## Requirements
- Raspberry Pi 4 or equivalent
- 1 x Breadboard
- 10 x Male to Female Jumper Wires
- 7 x Male to Male Jumper Wires
- 3 x 0.25W 100Ω Resistors
- 1 x LED
- 1 x DC Motor
- 1 x Transistor
- 2 x Physical Buttons

### 1 Button
If your setup only consists of 1 button to control both LED and the DC motor, you will only need
- 9 x Male to Female Jumper Wires
- 5 x Male to Male Jumper Wires
- 2 x 0.25W 100Ω Resistors
- 1 x Physical Button

## Connection Guide

### LED

### DC Motor
Because a typical motor requires 3V or 5V, the GPIO pins do not supply enough power. You need a transistor to supply additional power from a 5V pin on the Pi.

