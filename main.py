from moviepy.editor import *
import os

def convert_video(input_path, output_path):
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    # загружаем исходный файл
    video = VideoFileClip(input_path)

    # создаем новое имя файла для сохранения
    filename = os.path.splitext(os.path.basename(input_path))[0]
    output_file = os.path.join(output_path, f"{filename}.mp4")

    # конвертируем видео и сохраняем его в новый файл
    video.write_videofile(output_file, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    # замените путь до файла на ваш
    input_path = "C:\\Users\\user\\Videos\\video.flv"
    output_path = "C:\\Users\\user\\Videos\\Отконвертированно"
    convert_video(input_path, output_path)
    print('Конвертация завершена успешно')