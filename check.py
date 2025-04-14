import librosa
import numpy as np
import matplotlib.pyplot as plt

# Đọc âm thanh gốc và âm thanh đã giấu tin
audio_file_1 = 'input.wav'  # Đoạn âm thanh gốc
audio_file_2 = 'output_audio.wav'  # Đoạn âm thanh đã giấu tin

# Tải các tệp âm thanh và lấy tín hiệu sóng âm
y1, sr1 = librosa.load(audio_file_1, sr=None)  # sr=None giữ nguyên tần số mẫu của file gốc
y2, sr2 = librosa.load(audio_file_2, sr=None)  # sr=None giữ nguyên tần số mẫu của file giấu tin

# Kiểm tra độ dài của tín hiệu
if len(y1) != len(y2):
    # Cắt hoặc kéo dài tín hiệu để có cùng độ dài
    min_len = min(len(y1), len(y2))
    y1 = y1[:min_len]
    y2 = y2[:min_len]

# Tính toán sự khác biệt giữa tín hiệu gốc và tín hiệu đã giấu tin
difference = np.abs(y1 - y2)

# Tạo một mảng màu để đánh dấu sự thay đổi (đỏ cho sự khác biệt lớn, xanh cho không thay đổi)
threshold = 0.1  # Ngưỡng để đánh dấu sự thay đổi (có thể điều chỉnh)
colors = ['red' if diff > threshold else 'blue' for diff in difference]

# Tạo figure cho đồ thị
plt.figure(figsize=(12, 8))

# Đoạn A: Tín hiệu gốc
plt.subplot(2, 1, 1)
plt.plot(y1, color='blue', label='Tín hiệu gốc')
plt.title('Tín hiệu gốc')
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')

# Đoạn B: Tín hiệu đã giấu tin, với các điểm có sự khác biệt hiển thị đỏ
plt.subplot(2, 1, 2)
plt.plot(y2, color='blue', label='Tín hiệu đã giấu tin', alpha=0.5)  # Màu xanh cho toàn bộ
for i in range(len(y1)):
    if colors[i] == 'red':
        plt.plot(i, y2[i], 'ro', markersize=2)  # Vẽ điểm màu đỏ ở những chỗ có sự thay đổi

plt.title('Tín hiệu đã giấu tin với các điểm thay đổi được hiển thị đỏ') 
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()
