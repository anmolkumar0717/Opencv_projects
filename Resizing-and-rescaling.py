import cv2 as cv

def resize(frame,scale=0.5):
	height=700
	width=600
	dimension=(height,width)

	return cv.resize(frame,dimension)


capture=cv.VideoCapture("dog.mp4")
def changeres(width,height):
	capture.set(3,width)
	capture.set(4,height)


while True:
	istrue,frame1=capture.read()
	if (istrue):

		frame2=resize(frame1,0.2)
		cv.imshow("Resize-video",frame2)

		if (cv.waitKey(20)==ord('s')):
			break
	else:
		break

# img1=cv.imread('dog.jpg')
# img2=resize(img1,0.3)

# cv.imshow("Resize-image",img2)

# cv.waitKey(0)


