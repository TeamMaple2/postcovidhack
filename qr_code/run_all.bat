echo "===> running cafe_owner_qrcode.py"
python3 cafe_owner_qrcode.py --wallet 1Awyd1QWR5gcfrn1UmL8dUBj2H1eVKtQhg --amount 2.50 --balancecheck true
echo "===> running customer_qrcode.py"
python3 customer_qrcode.py --wallet 1234567890cfrn1UmL8dUBj2Awyd1QWR5g --qrinput data/cafe_owner_qr.png
echo "===> running cafeowner_send.py"
python3 cafeowner_send.py --qrinput data/customer_qr.png
