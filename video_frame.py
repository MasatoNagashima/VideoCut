import cv2
import os

def save_frame(video_name, _frame_num):
    video_path = 'original_video/' + video_name + '.mp4'
    result_path = 'output_image/mid_output/image-' + video_name + str(_frame_num) + '.jpg'

    cap = cv2.VideoCapture(video_path)
    video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    frame_num = int(video_frame_count // 4 * _frame_num )

    if not cap.isOpened():
        return

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    ret, frame = cap.read()

    if ret:
        os.makedirs(os.path.dirname(result_path), exist_ok=True)
        cv2.imwrite(result_path, frame)

def concat_img(video_name):
    img1 = cv2.imread('output_image/mid_output/image-' + video_name + '1.jpg')
    img2 = cv2.imread('output_image/mid_output/image-' + video_name + '2.jpg')
    img3 = cv2.imread('output_image/mid_output/image-' + video_name + '3.jpg')
    img4 = cv2.imread('output_image/mid_output/image-' + video_name + '4.jpg')

    img5 = cv2.hconcat([img1, img2, img3, img4])
    cv2.imwrite('output_image/final_output/image-' + video_name + '.jpg', img5)

def save_frame_all(video_name):
    for i in range(4):
        save_frame(video_name, i + 1)
    concat_img(video_name)

if __name__ == '__main__':
    save_frame_all('9_PBOptimization')