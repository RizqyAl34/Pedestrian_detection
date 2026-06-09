import cv2
import imutils
# Menginisialisasi orang HOG
# detektor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector(
))
# Membaca Gambar
image = cv2.imread('img.png')
# Mengubah ukuran gambar
image = imutils.resize(image,
width=min(400, image.shape[1]))
# Mendeteksi semua wilayah di
# Gambar yang memiliki pejalan kaki di dalamnya
(regions, _) = hog.detectMultiScale(image,
winStride=(4, 4),
padding=(4, 4),
scale=1.05)
# Menggambar wilayah dalam Gambar
for (x, y, w, h) in regions:
    cv2.rectangle(image, (x, y),
(x + w, y + h),
(0, 0, 255), 2)
# Menampilkan Gambar keluaran
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()