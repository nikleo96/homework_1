import struct
file_name = "flash.img"
file_name_out = "flash_out.img"
size_flesh = 7990149120
serial_number = "YT4411000602002000Y5"
serial_number = bytes(serial_number, "ascii")

print(serial_number)

with open(file_name, "rb") as f:
    text = f.read()

num_first_sector = text[454:458]
num = int((size_flesh - 512 * struct.unpack("I", num_first_sector)[0])/512)
num_hex = struct.pack("I", num)
text = text[:458] + num_hex + text[462:95420416] + serial_number + text[95420436:]

with open(file_name_out, "wb") as f:
    f.write(text)


    
