import cv2
import os

def save_frame(video_name, _frame_num):
    video_path = 'original_video/' + video_name + '.mp4'
    result_path = 'output_image/mid_output/image-' + video_name + str(_frame_num) + '.png'

    cap = cv2.VideoCapture(video_path)
    video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    frame_num = int(video_frame_count // 5 * (_frame_num))

    if not cap.isOpened():
        return

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    ret, frame = cap.read()

    if ret:
        os.makedirs(os.path.dirname(result_path), exist_ok=True)
        cv2.imwrite(result_path, frame)

def concat_img(video_name, _frame_num):
    img = cv2.imread('output_image/mid_output/image-' + video_name + str(_frame_num) + '.png')
    img_height = img.shape[0]
    img_width = img.shape[1]
    new_img = img[img_height//4: img_height//5 * 3, img_width//5 *2: img_width//3 * 2]
    cv2.imwrite('output_image/final_output/image-' + video_name + str(_frame_num) + '.png', new_img)

def save_frame_all(video_name):
    for i in range(4):
        save_frame(video_name, i + 1)
        concat_img(video_name, i + 1)

if __name__ == '__main__':
    save_frame_all('19_PegInHole')