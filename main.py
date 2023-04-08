# create by: yashar zavary rezaie
import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
while True:
    _, frame = cam.read()
    frame_y,frame_x,_= frame.shape
    frame=cv2.flip(frame, 1)
    rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    landmark_point=output.multi_face_landmarks
    screenw,screenh=pyautogui.size()
    if landmark_point:
        landmarks=landmark_point[0].landmark
        for lid,landmark in enumerate(landmarks[474:478]):
            x=int(landmark.x*frame_x)
            y=int(landmark.y*frame_y)
            cv2.circle(frame,(x,y),3,(0,255,0))
            if lid==1:
                move_x=landmark.x*screenw
                move_y=landmark.y*screenh
                pyautogui.moveTo(move_x,move_y)
        lefteye=[landmarks[145],landmarks[159]]
        if (lefteye[0].y - lefteye[1].y) <0.004:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow("eye control", frame)
    cv2.waitKey(1)
