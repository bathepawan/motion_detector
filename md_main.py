import cv2
import numpy as np
from datetime import datetime


def look_for_motion():
    '''
    Simple motion detector from a video feed on webcam.
    It's working is simple , take a diff of two consecutive frames,
     and average out the diff , in case of no motion , average is expected to be close to zero.
     with experiement and few trial and error runs, found out that 5 act as good threshold for motion detection
    :return: None
    '''

    video_stream = cv2.VideoCapture(0)

    ret, curr_frame = video_stream.read()

    while True:
        last_frame = curr_frame

        ret, curr_frame = video_stream.read()

        diff = cv2.absdiff(last_frame, curr_frame)
        delta = np.mean(diff)
        timestamp = datetime.now()
        if delta > 5:
            print('Delta {} is greater than a threshold, motion detected'.format(delta))
            cv2.imwrite("{}_before.jpg".format(timestamp), last_frame)
            cv2.imwrite('{}_after.jpg'.format(timestamp), curr_frame)

        cv2.imshow('Live Feed', curr_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_stream.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':

    look_for_motion()
