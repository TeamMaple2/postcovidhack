import qrcode
import argparse
import cv2
import json

def sign(text):
    return "SIGNED"+text+"SIGNED"

my_parser = argparse.ArgumentParser()

my_parser.add_argument('-w', '--wallet', help='cafe owner\'s wallet')
my_parser.add_argument('-q', '--qrinput', help='qr code input file')

args = my_parser.parse_args()
print("qrinput:", args.qrinput)
img = cv2.imread(args.qrinput)

detector = cv2.QRCodeDetector()
decodedText, _, _ = detector.detectAndDecode(img)
data = json.loads(decodedText)

transaction = "TX:From:" + args.wallet +", to:"+ data['wallet_address']+ ", amount=" + str(data['amount'])
newData = {
    'signed_transaction': sign(transaction),
    'balancecheck': data['balancecheck']
}
qrtext = json.dumps(newData)
print("qrtext:", qrtext)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # ERROR_CORRECT_L:7% errors didn't work, hence using M:15% error
    box_size=10,
    border=4,
)
qr.add_data(qrtext)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

qrcodepath = 'data/customer_qr.png'
img.save(qrcodepath)
print("Customer QR code created " + qrcodepath)
