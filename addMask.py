from imutils import face_utils
import numpy as numpy
import imutils
import dlib
import cv2

def mask(image):
	left_end = 3
	bottom_end = 8

	left_end_mask = [1, 135]
	bottom_end_mask = [140, 285]

	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

	image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
	mask = cv2.imread('mask.png')
	image = imutils.resize(image, width=500)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faces = detector(gray, 1)

	for(i, face) in enumerate(faces):
		facial_points = predictor(gray, face)

		facial_points = face_utils.shape_to_np(facial_points)

		width_face = 2*(facial_points[bottom_end][0] - facial_points[left_end][0])
		height_bottom_face = facial_points[bottom_end][1]- facial_points[left_end][1]

		ratio = (bottom_end_mask[1] - left_end_mask[1])/height_bottom_face

		height_face = height_bottom_face + int(left_end_mask[1]/ratio)

		mask_resize = cv2.resize(mask, (width_face, height_face))

		w, h, c = mask_resize.shape

		start_face_x = facial_points[left_end][0]
		start_face_y = facial_points[left_end][1] - int(left_end_mask[1]/ratio)

		for k in range(0, w):
			for j in range(0, h):
				if mask_resize[k, j][2] != 0:
					image[start_face_y+k, start_face_x+j] = mask_resize[k, j]

	retval, buffer = cv2.imencode('.jpg', image)
	return buffer
