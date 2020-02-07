# Import Necessary Libraries
import numpy as np
import cv2

def removeBackground():
	cap = cv2.VideoCapture('test2.mov')
	# Initlaize background subtractor
	foreground_background = cv2.createBackgroundSubtractorMOG2()

	# Infinite Loop and breaks when Enter is pressed
	while True:
	    ret, frame = cap.read()
	    # Apply background subtractor to get our foreground mask
	    foreground_mask = foreground_background.apply(frame)
	    cv2.imshow('Output', foreground_mask)
	    if cv2.waitKey(1) == 27:
	        break
	        cv2.destroyAllWindows()

	# Destroy All Windows and release capture instance
	cap.release()
	cv2.destroyAllWindows()