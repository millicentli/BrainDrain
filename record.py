import cv2
import acapture
import pyautogui

# Video cam recording
cap = acapture.open(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

# print(cap.get(5))
fps = 29.000049

capture_size = (1280, 720)
out = cv2.VideoWriter('output.avi', fourcc, fps, capture_size)
pyautogui.keyDown('shift')
pyautogui.keyDown('command')
pyautogui.press('5')
pyautogui.keyUp('command')
pyautogui.keyUp('shift')
pyautogui.click()

buf = []
while cv2.waitKey(1) & 0xFF != ord('q'):
    check, frame = cap.read()
    if check:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Write the frame
        out.write(frame)
        # buf.append(frame)
        cv2.imshow('frame', frame)

print("stopping")

# Stop the recording
pyautogui.keyDown('command')
pyautogui.keyDown('ctrl')
pyautogui.press('esc')

# Release everything if job is finished
cap.destroy()
out.release()
cv2.destroyAllWindows()
