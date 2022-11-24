import asyncio
import logging
from sys import argv

from growattRS232 import GrowattRS232
# InfluxDB imports
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# defaults
# USB port of RS232 converter
DEFAULT_PORT = "COM3"
# Growatt modbus address
DEFAULT_ADDRESS = 0x1

logging.basicConfig(level=logging.DEBUG, filename='debug_log.log', filemode='w')



async def main():
    port = str(argv[1]) if len(argv) > 1 else DEFAULT_PORT
    address = int(argv[2]) if len(argv) > 2 else DEFAULT_ADDRESS
    growattRS232 = GrowattRS232(port, address)
    token = os.environ.get("INFLUXDB_TOKEN")
    org = "YOUR_ORG"
    bucket="YOUR_BUCKET"
    url = "http://YOUR_INFLUXDB_IP:PORT/"
    try:
        # Export data to InfluxDB
        client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
        write_api = client.write_api(write_options=SYNCHRONOUS)
        # Get data every second for 5 times
        for value in range(5):
            data = await growattRS232.async_update()
            # Not set on how this should be formatted yet
            point = [{"measurement": "growatt2", "tags": {"serial_number": data['serial_number'], "model_number": data['model_number'], "port": port, "address": address}, "fields": data}]
            write_api.write(bucket=bucket, org=org, record=point)
            time.sleep(1) # separate points by 1 second
        
    except Exception as error:
        print("Error: " + repr(error))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
