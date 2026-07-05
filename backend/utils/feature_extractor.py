import cv2

def extract_features(image_path):

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    orb = cv2.ORB_create(nfeatures=500)

    keypoints, descriptors = orb.detectAndCompute(image, None)

    return keypoints, descriptors