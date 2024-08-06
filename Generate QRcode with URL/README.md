</h1>QR Code Generator</h1>
<h2>hThis project is simple generate QRcode from URL by specific URL and save as URL name.</h2>

<h2>Prerequiresite</h2>
- Python 3.x
- pyqrcode library

<h3>Installation</h3>
Install python qrocode library.
```
pip install pyqrcode
```

<h3>Usage</h3>
1. Run the Python script.
2. Enter URL.
3. The QR code will be generated and saved as a png file named [your_URL].png

<h3>Example</h3>
```
$ python genQRcodewURL.py
Enter the URL to be converted to QR code: https://www.abcd.com
QR code has been generated and saved as 'httpswwwabcdcom.png'
```
This will generate a QR code for the URL "https://www.abcd.com" and save it as "httpswwwabcdcom.png".

<h3>Notes</h3>
- The QR code is generated using the pyqrcode library.
- The generated QR code is saved as an PNG file for web-quality output.
- The scale of the QR code can be adjusted by changing the scale parameter in the qr.png() function.
