from imutils.video import VideoStream
from pyzbar import pyzbar

import imutils
import time
import cv2

from qr_match import match

def barcode_scanner():
	print("[INFO] starting video stream...")
	#vs = VideoStream(src=0).start()
	vs = VideoStream(usePiCamera=True).start()
	time.sleep(2.0)

	while True:
		frame = vs.read()
		frame = imutils.resize(frame, width=400)

		barcodes = pyzbar.decode(frame)
		cv2.imshow("Barcode Scanner", frame)
		

		for barcode in barcodes:
			(x, y, w, h) = barcode.rect
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
			barcodeData = barcode.data.decode("utf-8")

			match(barcodeData)

		
		key = cv2.waitKey(1) & 0xFF

		if key == ord("q"):
			break

	print("[INFO] cleaning up...")
	cv2.destroyAllWindows()
	vs.stop()

barcode_scanner()
