import zlib

file_path = "./Ayn Rand - The Fountainhead.epub.an"

with open(file_path, 'rb') as file:
    binary_data = file.read()

try:
    decompressed_data = zlib.decompress(binary_data)
    print(decompressed_data.decode('utf-8', errors='replace').split("\n\n")[4].split("\n")[1])
except zlib.error as e:
    print(f"Decompression failed: {e}")
