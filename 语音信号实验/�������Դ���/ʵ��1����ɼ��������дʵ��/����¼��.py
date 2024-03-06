import pyaudio # 导入 Pyaudio 库
import wave # 导入 wave 库
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

CHUNK = 1024 # 设定缓存区帧数为 1024 
FORMAT = pyaudio.paInt16 # 设定数据流采样深度为 16 位
CHANNELS = 2 # 设置声卡通道为 2 
RATE = 16000 # 设置采样率
RECORD_SECONDS = 5 # 设置记录秒数
pa = pyaudio.PyAudio() # 实例化一个 Pyaudio 对象
stream = pa.open( format=FORMAT, channels=CHANNELS, rate=RATE, input=True, 
frames_per_buffer=CHUNK) 
print("* recording") # 打印开始“录音”标志
frames = [] # 创建一个新列表，用于存储采集到的的数据
#开启循环采样直至采集到所需的样本数量
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)): 
 data = stream.read(CHUNK) # 从数据流中读取样本
 frames.append(data) # 将该样本记录至列表中
print("* done recording") # 打印“完成录音”标志
stream.stop_stream() # 关闭数据流
stream.close() # 关闭声卡
pa.terminate()
# 保存录音数据为WAV文件
filename = "C2_1_y_1.wav"
wf = wave.open(filename, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(pa.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print(f"录音已保存为 {filename}")