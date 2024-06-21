import google.generativeai as genai



def gemini_configure():
    key = 'AIzaSyAhEe_ErZpxOw6bakv_EfmxIL6B2_HHJdI'
    genai.configure(api_key=key)  # 配置 API 金鑰

def select_model(model_name="gemini-1.5-flash-latest") :  
    return genai.GenerativeModel(model_name=model_name)  # 創建生成式 AI 模型




def recognize_speech(audio_file_name):  # 定義語音識別函數，接收聲音檔案名作為參數
    gemini_configure()
    model = select_model(model_name="gemini-1.5-flash-latest")
    audio_file = genai.upload_file(path=audio_file_name)  # 上傳聲音文件
    response = model.generate_content(["please translate given words to english", audio_file])  # 使用模型生成內容
    
    return response.text  # 返回生成內容