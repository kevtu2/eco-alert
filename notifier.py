import serial
import time
from winotify import Notification


def setup_arduino():

    arduino_port = 'COM7'
    baud_rate = 9600

    ser = serial.Serial(arduino_port, baud_rate)
    time.sleep(5) # wait

    if ser.is_open:
        print(f"Established connection to {arduino_port}.")
        return ser;

def send_notification()->bool:
    toast = Notification(app_id="Eco-Alert",
                         title="Warning! Possible unintended energy usage.",
                         msg="You have left a device on in the other room. Please turn off any unnecessary or non-critical devices",
                         duration="long")
    toast.show()
    return True


def main():
    ser = setup_arduino()
    motion = 0
    device_on_off = 0
    sent = False

    if (ser.is_open):
        while True:
            if ser.in_waiting > 0:
                motion = ser.readline().decode('utf-8').strip() # detected (1) or not detected (0)
                device_on_off = ser.readline().decode('utf-8').strip() # on (1) or off (0)
                print(f"Motion: {motion}, device_status: {device_on_off}")

            # Using extra energy for no reason!!
            if motion == "0" and device_on_off == "1" and not sent:
                sent = send_notification()
            # Reset
            elif motion == "0" and device_on_off == "0" and sent:
                sent = False
                

if  __name__ == "__main__":
    main()