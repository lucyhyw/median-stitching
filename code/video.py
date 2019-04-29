import numpy as np
import cv2

cap = cv2.VideoCapture('../data/green.mov')
allFrames = []
# frames = np.arange(0, 10800, 15)
frames = np.arange(0, 2250, 15)
frames = np.reshape(frames, (-1, 10))
frames = np.transpose(frames)
# print(frames)
# count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    allFrames.append(frame)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
allFrames = np.array(allFrames)
print(allFrames.shape)
framesWeWant = allFrames[frames]
print(framesWeWant)

# print(everyFiveFrames)

cap.release()
cv2.destroyAllWindows()
