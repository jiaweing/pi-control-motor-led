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

![image](https://github.com/jiaweing/pi-control-motor-led/assets/33184869/b2d82a26-b946-4367-820a-56fb17a25e05)

### LED
Use the left side of the breadboard.
1. Connect the top of the positive (+) rail to number 2.
2. Connect the top of the negative (-) rail to number 6.
3. Connect A1 to GPIO18.
4. Insert a resistor into B1 and B4.
5. Connect B5 to the negative rail.
6. Put the long leg (+) of the LED into E4 (same column as resistor B4) and the shorter leg (-) in E5 (same column as 5).

### Button
Use the left side of the breadboard.
1. Insert a button onto the board.
3. Insert a resistor into C23 (same column as positive side of the button) and C28.
4. Connect B21 to the negative rail. (same column as negative side of button)
5. Connect B23 to GPIO23. (same column as positive side of button)
6. Connect A28 (same column as resistor C28) to the negative rail.

### DC Motor
Because a typical motor requires 3V or 5V, the GPIO pins do not supply enough power. You need a transistor to supply additional power from a 5V pin on the Pi. Use the right side of the breadboard.

1. Connect the top of the positive (+) rail to number 4.
2. Connect the top of the negative (-) rail to number 9.
1. Connect a wire from the left board's negative rail to the right board's negative rail.
2. Insert the transistor with the flat edge facing towards the right side of the board. (F6 - F4)
3. Connect I5 (same column as transistor middle leg) to GPIO24.
4. Connect J6 (same column as transistor left leg) to the negative rail.
5. Connect J4 (same column as transistor right leg) to the negative wire of the motor.
6. Connect the positive wire of the motor to the positive rail.
