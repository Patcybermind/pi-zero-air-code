import time
import busio # type: ignore    
import digitalio # type: ignore
import board # type: ignore
import microcontroller # type: ignore
import adafruit_rfm9x # type: ignore


sleep_time = 0
current_time = 1

while current_time <= sleep_time:
    print("Sleeping for {0} seconds".format(sleep_time - current_time))
    time.sleep(1)
    current_time += 1

RADIO_FREQ_MHZ = 868.0  # Frequency of the radio in Mhz. Must match your

# Create library object using our bus SPI port for radio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# RFM9x Breakout Pinouts
CS = digitalio.DigitalInOut(board.D27)
RESET = digitalio.DigitalInOut(board.D22)

CS.direction = digitalio.Direction.OUTPUT
RESET.direction = digitalio.Direction.OUTPUT

# wait for spi to be ready
spi.try_lock()

spi.configure(baudrate=100_00)

# might need to then do spi.unlock()

print("spi done configuring and spi baudrate set")

rfm9x.tx_power = 8 # change later

sleep_time = 1000
current_time = 0
while current_time <= sleep_time:
    print("Sleeping for {0} seconds".format(sleep_time - current_time))
    time.sleep(.5)
    current_time += 1
    rfm9x.send(bytes("Hello world!\r\n", "utf-8"))
    print("Sent Hello World message!")



