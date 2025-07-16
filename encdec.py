import codecs
from base64 import b64encode, b64decode
import argparse

parser = argparse.ArgumentParser(description="EncDec is a program that allows you to encode and decode text using methods like ROT13, Base64, and hexadecimal.")
#parser.add_argument("-r13", "--rot13", help="rot13", action="store_true")
# parser.add_argument("-bs64", "--base64", help="base64", action="store_true")

parser.add_argument("-t", "--type", help="base64 / rot13 / hex")
parser.add_argument("-m", "--message", help="message", required=True)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-e", "--encode", help="encode", action="store_true")
group.add_argument("-d", "--decode", help="decode", action="store_true")


args = parser.parse_args()

class Rot13Engine:
    def __init__(self, text):
        self.text = text

    def rot13_encoder(self):
        # text = "this is a test"
        encode = codecs.encode(self.text, "rot13")
        return encode

    def rot13_decoder(self):
        # text = ""
        decode = codecs.decode(self.text, "rot13")
        return decode

class Base64Engine:
    # base64 operates on bytes, not directly on Unicode strings. Need to convert strings to bytes first, then decode it
    def __init__(self, text):
        self.text = text

    def base64_encoder(self):
        # convert string to bytes first
        data_bytes = self.text.encode("utf-8")

        # perform the operation
        encode_data = b64encode(data_bytes)

        # convert bytes back to strings
        data_strings = encode_data.decode()

        return  data_strings

    def base64_decoder(self):
        # convert string to bytes first
        data_bytes = self.text.encode("utf-8")

        # perform the operation
        decode_data = b64decode(data_bytes)

        # convert bytes back to strings
        data_strings = decode_data.decode()

        return data_strings

class HexEngine:
    def __init__(self, text):
        self.text = text

    def hex_encoder(self):
        # convert string to bytes first
        data_bytes = self.text.encode("utf-8")

        # perform the operation
        encode_data = codecs.encode(data_bytes, "hex")

        # convert bytes back to strings
        data_strings = encode_data.decode()

        return data_strings

    def hex_decoder(self):
        # convert string to bytes first
        data_bytes = self.text.encode("utf-8")

        # perform the operation
        decode_data = codecs.decode(data_bytes, "hex")

        # convert bytes back to strings
        data_strings = decode_data.decode()

        return data_strings

def main():
    # rot13
    if args.type.lower() == "rot13":
        if args.encode:
            # print("rot encode")
            output = Rot13Engine(args.message).rot13_encoder()
            print(output)

        elif args.decode:
            # print("rot decode")
            output = Rot13Engine(args.message).rot13_decoder()
            print(output)

    # base64
    elif args.type.lower() == "base64":
        if args.encode:
            # print("base encode")
            output = Base64Engine(args.message).base64_encoder()
            print(output)

        elif args.decode:
            # print("base decode")
            output = Base64Engine(args.message).base64_decoder()
            print(output)

    # hex
    elif args.type.lower() == "hex":
        if args.encode:
            # print("base encode")
            output = HexEngine(args.message).hex_encoder()
            print(output)

        elif args.decode:
            # print("base decode")
            output = HexEngine(args.message).hex_decoder()
            print(output)

if __name__ == "__main__":
    main()