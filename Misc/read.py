import cv2

# img = cv2.imread('Photos/cat_large.jpg')
# cv2.imshow('Cat', img)
# cv2.waitKey(0)

capture = cv2.VideoCapture('Videos/dog.mp4')

def reframe(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

while True:
    isTrue, frame = capture.read()
    frame_resized = reframe(frame)
    cv2.imshow('Video', frame)
    cv2.imshow('Video Resized', frame_resized)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()