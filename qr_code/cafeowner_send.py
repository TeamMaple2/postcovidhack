import qrcode
import argparse
import cv2
import json

my_parser = argparse.ArgumentParser()

my_parser.add_argument('-q', '--qrinput', help='qr code input file')

args = my_parser.parse_args()
print("qrinput:", args.qrinput)
img = cv2.imread(args.qrinput)

detector = cv2.QRCodeDetector()
decodedText, _, _ = detector.detectAndDecode(img)
data = json.loads(decodedText)

print("decodedText:", decodedText)
print("balanceCheck:", data['balancecheck'])

print("Sending decodedText to server")
