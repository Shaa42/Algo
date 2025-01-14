from math import ceil
from main import HuffmanCoding

def _to_Bytes(data):
    # https://stackoverflow.com/questions/51425638/how-to-write-huffman-coding-to-a-file-using-python
    b = bytearray()
    for i in range(0, len(data), 8):
        b.append(int(data[i:i+8], 2))
    return bytes(b)

def compress_file(input_file, output_file):
    # Read file to buffer
    text = ''
    with open(input_file, 'r') as f:
        for line in f:
            text += line
    
    # Compress using huffman coding
    binary_string = HuffmanCoding(text)
    
    # Write to new file
    with open(output_file, "wb") as nf:
        nf.write(_to_Bytes(binary_string))
        
    # Informations
    print(f"Original file size : {len(text)} bytes")
    print(f"New file size : {ceil(len(binary_string)/8)} bytes")

if __name__ == '__main__':
    compress_file("input.txt", "output.bin")