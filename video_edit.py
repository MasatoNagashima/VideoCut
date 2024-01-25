import os
import cv2
import time


def video_speed_change(path_in, path_out, scale_factor, color_flag):
    # 動画読み込みの設定
    movie = cv2.VideoCapture(path_in)

    # 動画ファイル保存用の設定
    # 元動画のFPSを取得
    fps = int(movie.get(cv2.CAP_PROP_FPS))

    # 動画保存時のFPSはスケールファクタをかける
    fps_new = int(fps * scale_factor)

    # 動画の横幅を取得
    width = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))

    # 動画の縦幅を取得
    height = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 動画保存時のfourcc設定（mp4用）
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

    # 動画の仕様（ファイル名、fourcc, FPS, サイズ）
    video = cv2.VideoWriter(path_out, fourcc, fps_new, (width, height), color_flag)  

    # ファイルからフレームを1枚ずつ取得して動画処理後に保存する
    while True:
        # フレームを取得
        ret, frame = movie.read()        

        # 動画を保存する
        video.write(frame)

        # フレームが取得できない場合はループを抜ける
        if not ret:
            break

    # 撮影用オブジェクトとウィンドウの解放
    movie.release()
    return

def video_speed_change_all():
    start = time.time()

    #読み込みたいフォルダまで移動
    original_path = "original_video/"
    faster_path = "faster_video/"
        
    #ファイル一覧取得
    files = os.listdir(original_path)

    for change_speed in files:
        path_in = original_path + change_speed

        # 保存する動画のパス
        path_out = faster_path + "faster_" + change_speed

        # FPSにかけるスケールファクター
        scale_factor = 4.0

        # カラー動画はTrue, グレースケール動画はFalse
        color_flag = True               

        # 動画の再生速度を変更する関数を実行
        video_speed_change(path_in, path_out, scale_factor, color_flag)
        print(f"{change_speed}の処理が完了しました。")

    total = time.time() - start

    print("処理が完了しました。")
    print("処理時間：" + str(total) + "[sec]")

if __name__ == '__main__':
    video_speed_change_all()