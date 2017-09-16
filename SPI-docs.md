SPI for python is already decently documented here: http://tightdev.net/SpiDev_Doc.pdf

The only 2 that really "matter" for our ADC is xfer and xfer2. By "perform SPI transaction" it basically means that xfer/xfer2
both "read and write bytes." When the clock signal hits a falling edge (go's to logic 0) the device will write the bytes passed into 
the parameters. When the lcock signal hits a rising edge (go's to logic 1) the device will read the master device (what the pi processes)
bytes back. For our ADC we give the pi 2 bytes with xfer, and we get 2 bytes back. 8 bits in a byte.

**EX of xfer2 usage** 

raw_data = spi.xfer2([2, 4, 120]) #this means we are passing binary values [00000010, 00000100, 1111000]



#we can then access 3 bytes in this case, raw_data is just an array of the bytes we get back
print(raw_data[2]) #prints 3rd byte. We have no way of knowing what it is, depends on the device were using!


xfer or xfer2: For our purposes these are interchangable. Xfer2 will keep CS asserted between blocks whereas xfer will reassert it.
Since we aren't moving our CS (CE0 and CE1) ALWAYS USE XFER2

TLDR: use xfer2

**MCP3002 ADC**

MCP3002 datasheet: http://ww1.microchip.com/downloads/en/DeviceDoc/21294E.pdf

1. Our adc takes/sends 2 bytes (since it only has 2 channels it is more compact than the other mcp adc models which do 3 bytes)

2. ALWAYS set the MSBF flag to 0 to show the MSB (most significant bit) first. This is the "default" way binary is read. If you really
wanted LSB bit first go ahead and set it to 1.

3. ALWAYS use Single-Ended mode for a channel over Differential-Mode. Single-Ended mode will run faster and stabler. Differential-Mode 
is useful if a lot of noise (lot's of thing can cause this one being a really long cable).

4. Channel 0 = 2'b10  and  Channel 1 = 2'b11  (both single-ended mode).

5. Though I said our device gets 2 bytes back only 10 of those bits have any meaning. We have to manually extract those 10 bits.



