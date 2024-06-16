
import os  # 導入 os 模組，用於操作文件和目錄
import uuid  # 導入 uuid 模組，用於生成唯一的文件名

from elevenlabs import VoiceSettings  # 從 elevenlabs 模組中導入 VoiceSettings 類
from elevenlabs.client import ElevenLabs  # 從 elevenlabs.client 模組中導入 ElevenLabs 類



def text_to_speech_file(text: str) -> str:


    eleven_key = ''

    ELEVENLABS_API_KEY = eleven_key  # 設定 ElevenLabs 的 API 金鑰

    client = ElevenLabs(
        api_key=ELEVENLABS_API_KEY,
    )  # 創建 ElevenLabs 客戶端對象
    response = client.text_to_speech.convert(
        voice_id="RM1LAdUB7ksnpreLvjxR",
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,  # 要轉換的文本
        model_id="eleven_turbo_v2",  # 使用 turbo 模型以獲得快速取得轉換結果，對於其他語言使用 `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),  # 聲音設置
    )

    save_file_path = f"{uuid.uuid4()}.mp3"  # 生成唯一的文件名

    with open(save_file_path, "wb") as f:  # 打開文件以寫入數據
        for chunk in response:
            if chunk:
                f.write(chunk)  # 將每個數據塊寫入文件

    print(f"新音頻文件已成功保存到 {save_file_path}")  # 提示音頻文件保存成功
    return save_file_path  # 返回保存的文件路徑