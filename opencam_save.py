# import the opencv library
import cv2
import datetime
  
# define a video capture object
vid = cv2.VideoCapture(0)

#recording variables
record = False
fourcc = cv2.VideoWriter_fourcc(*'XVID')
now = ''
stamp = ''

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    KeyCode = cv2.waitKey(1) & 0xFF
    if KeyCode == ord('q'):
        break
    elif KeyCode == ord('r'):
        print("recording start")
        now = datetime.datetime.now().strftime("%d_%H-%M-%S")
        record = True
        video = cv2.VideoWriter("Savevid/" + str(now) + ".avi", fourcc, 30.0, (frame.shape[1], frame.shape[0]))
    elif KeyCode == ord('s'):
        print("recording finished")
        record = False
        video.release()
    if record == True:
        if stamp != datetime.datetime.now().strftime("%d_%H-%M-%S"):
            print("recording process...")
        video.write(frame)
        stamp = datetime.datetime.now().strftime("%d_%H-%M-%S")

  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
