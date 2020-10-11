import qrcode
import argparse
import json

my_parser = argparse.ArgumentParser()

my_parser.add_argument('-w', '--wallet', help='cafe owner\'s wallet') #, required=True)
my_parser.add_argument('-a', '--amount', help='amount in euros', type=float)
my_parser.add_argument('-b', '--balancecheck', help='balance check required')

args = my_parser.parse_args()

data = {
  'wallet_address': args.wallet,
  'amount': args.amount, 
  'balancecheck': args.balancecheck
}
qrtext = json.dumps(data)
print("qrtext:", qrtext)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(qrtext)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

qrcodepath = 'data/cafe_owner_qr.png'
img.save(qrcodepath)

print("Cafe owner QR code created " + qrcodepath)