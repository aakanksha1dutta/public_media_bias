from imutils import paths
import argparse
import cv2

from imutils import paths
import argparse
import cv2

#cv2.CV_64F is the laplacian kernel used
def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-t1", "--threshold1", type=float, default=120.0,
	help="focus measures that fall below this value will be considered 'blurry'")
ap.add_argument("-t2", "--threshold2", type=float, default=400.0,
	help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

# loop over the input images
for imagePath in paths.list_images(args["images"]):
	image = cv2.imread(imagePath) #read images
	image = cv2.resize(image, (640,640))
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to grayscale
	fm = variance_of_laplacian(gray) 
	text = "Not Blurry"
	# if the focus measure is less than the supplied threshold,
	# then the image should be considered "blurry"
	if fm < args["threshold1"]:
		text = "Very Blurry"
	elif fm < args["threshold2"]:
		text = "Somewhat Blurry"
		
	# show the image
	if text=='Not Blurry':
		cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
			cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
		cv2.imshow("Image", image)
		key = cv2.waitKey(0)