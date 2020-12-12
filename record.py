import numpy as np
import cv2
import pyautogui

# Video cam recording
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

fps = 20
capture_size = (int(cap.get(3)), int(cap.get(4)))
out = cv2.VideoWriter('output.avi', fourcc, fps, capture_size)
pyautogui.keyDown('shift')
pyautogui.keyDown('command')
pyautogui.press('5')
pyautogui.keyUp('command')
pyautogui.keyUp('shift')
pyautogui.click()

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # Write the frame
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

# Stop the recording
pyautogui.keyDown('command')
pyautogui.keyDown('ctrl')
pyautogui.press('esc')
