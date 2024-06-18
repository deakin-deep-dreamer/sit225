import sys
import traceback
import random
from arduino_iot_cloud import ArduinoCloudClient
import asyncio

DEVICE_ID = "bc5c0fe9-e6ef-4eb0-90de-05032ffd9a83"
SECRET_KEY = "3oJYfrkmSNjM4YwKGJgVObbBn"
btn_status_active = False


def read_value():
    return random.randint(0, 100)

def on_temperature_changed(client, value):
    print(f"New temperature: {value}")

def main():
    print("main() function")
    client = ArduinoCloudClient(
        device_id=DEVICE_ID, username=DEVICE_ID, password=SECRET_KEY
    )
    # client.register("test_value")
    # client["test_value"] = read_value()
    client.register("temperature", value=None, on_write=on_temperature_changed)
    client.start()

if __name__ == "__main__":
    try:
        main()
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_type, file=print)