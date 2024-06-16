# -*- coding: utf-8 -*-
# import sounddevice as sd  # 導入 sounddevice 模組，用於聲音錄製
# from scipy.io.wavfile import write  # 從 scipy.io 模組中導入 write 函數，用於保存 WAV 文件
# import numpy as np  # 導入 numpy 模組，便於處理數據
# from IPython.display import Audio, display
import google.generativeai as genai
from audio import record
from api.gemini import fetch
from text_to_speech.eleven_labs import txt_to_speech




def sound(audio_file_path):
    duration = 3600  # 設定錄音時長為 3600 秒（1 小時）
    audio, sample_rate = record.record_audio(duration)  # 錄製聲音

    if audio.size > 0:  # 如果錄製到了聲音
        record.save_audio(audio = audio, sample_rate = sample_rate, filename = audio_file_path)  # 保存聲音
        return 1
    else:
        print("未錄製到聲音。")  # 提示未錄製到聲音
        return 0

    """## 播放錄音檔案"""

    # audio = Audio(filename=audio_file_path, autoplay=True)  # 創建 Audio並設定自動播放
    # display(audio)  # 顯示聲音播放控制項
    return audio_file_path


def call_gemini_api(audio_file_path='output.wav'):

    translated_text = fetch.recognize_speech(audio_file_path)
    
    return translated_text

def call_elevenlabs_api(translated_text):

    fpath = txt_to_speech.text_to_speech_file(translated_text)
    
    return fpath

if __name__ == '__main__':
    audio_file_path = "output.wav"
    
    record_sucess = sound(audio_file_path = "output.wav")
    if record_sucess:
        translated_text = call_gemini_api(audio_file_path)
        print(translated_text)    

    # """## 使用Elevenlabs 合成聲音"""
        fpath = call_elevenlabs_api(translated_text)
        print(fpath)
        
    else:
        print("未錄製到聲音")

    # from IPython.display import Audio, display

    # audio_file_path = fpath

    # audio = Audio(filename=audio_file_path, autoplay=True)  # 創建 Audio並設定自動播放
    # display(audio)  # 顯示聲音播放控制項




