import sounddevice as sd  # 導入 sounddevice 模組，用於聲音錄製
from scipy.io.wavfile import write  # 從 scipy.io 模組中導入 write 函數，用於保存 WAV 文件
import numpy as np  # 導入 numpy 模組，便於處理數據

def record_audio(duration, sample_rate=44100):
    print("正在錄音... 按 Ctrl+C 停止錄音。")
    audio = np.empty((0, 1), dtype=np.int16)  # 初始化一個空的聲音

    try:
        with sd.InputStream(samplerate=sample_rate, channels=1, dtype='int16') as stream:  # 打開輸入聲音
            for _ in range(int(sample_rate * duration / 1024)):  # 將時長分成多個小塊進行錄製
                data, overflowed = stream.read(1024)  # 讀取 1024 個樣本的聲音
                audio = np.append(audio, data, axis=0)  # 將新數據追加到聲音中
    except KeyboardInterrupt:  # 捕捉用戶中斷錄音的操作
        print("\n錄音被用戶中斷。")

    return audio, sample_rate  # 返回錄製的聲音和採樣率

def save_audio(audio, sample_rate, filename="output.wav"):
    write(filename, sample_rate, audio)  # 保存聲音數據到指定的文件中
    print(f"音訊已保存至 {filename}")  # 提示聲音已保存