import sys

if len(sys.argv) < 2:
    sys.exit("No file provided")

print("Using file: ", sys.argv[1])

try:
    with open(sys.argv[1], "rb") as f:
        f.seek(65)
        pw = ""
        byte = f.read(1)[0]
        while byte != 0:
            if byte <= 10:
                pw += chr(byte + 47)
            elif byte <= 36:
                pw += chr(byte + 54)
            elif byte <= 62:
                pw += chr(byte + 60)
            byte = f.read(1)[0]
        
        print("Extracted password: ", pw)
except IOError:
    sys.exit("Error opening file: ", sys.argv[1])
except Exception as e:
    sys.exit(e)