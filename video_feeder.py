import numpy as np
import cv2



cap = cv2.VideoCapture('sample_video.mpeg')
ret, frame = cap.read()
frame_size = frame.shape

def get_sequence(seq_length, img_size=None):
    global cap
    if img_size:
        sequence = np.zeros((seq_length, img_size[0], img_size[1], frame_size[2]))
    else:
        sequence = np.zeros((seq_length, frame_size[0], frame_size[1], frame_size[2]))

    for i in range(seq_length):

        if not cap.isOpened():
            cap.release()
            cap = cv2.VideoCapture('sample_video.mpeg')
            i = 0

        ret, frame = cap.read()
        print(frame.shape)
        print(sequence[0].shape)

        if img_size is None:
            sequence[i] = frame
        else:
            sequence[i] = cv2.resize(frame, img_size)


        #sequence[i] = frame

    return sequence



def get_data(batch_size, seq_length=10, img_size=None):
    counter = 0
    height = img_size[0] if img_size else frame_size[0]
    width = img_size[1] if img_size else frame_size[1]
    channels = frame_size[2]

    frame_buffer = np.zeros((batch_size, seq_length, height, width, channels))
    for i in range(batch_size):
        frame_buffer[i] = get_sequence(seq_length, img_size)
    return frame_buffer

batch_size = 32
seq_length = 2
img_size = (64, 64)
frame_buffer = get_data(batch_size, seq_length, img_size)
