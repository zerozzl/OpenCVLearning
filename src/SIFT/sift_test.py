import cv2

img = cv2.imread('/home/zero/Pictures/lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
kp = sift.detect(gray, None)

img = cv2.drawKeypoints(gray, kp, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite('/home/zero/Pictures/lena_sift.jpg', img)

print 'SIFT Complete'
