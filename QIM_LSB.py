import numpy as np
import soundfile as sf

# Hàm chuyển văn bản thành nhị phân
def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

# Đọc tệp văn bản
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Hàm nhúng thông điệp bằng LSB
def lsb_embed(audio, binary_message):
    stego_audio = np.copy(audio)
    # Chuyển đổi âm thanh sang kiểu int trước khi sử dụng bitwise
    audio_int = np.int16(audio * 32767)  # Chuyển đổi giá trị float32 sang int16
    for i in range(len(binary_message)):
        # Thực hiện bitwise trên dữ liệu int16
        stego_audio[i] = (audio_int[i] & ~1) | int(binary_message[i])
    return stego_audio

# Hàm nhúng thông điệp bằng QIM
def qim_embed(audio, binary_message, delta=0.001):
    stego_audio = np.copy(audio)
    for i, bit in enumerate(binary_message):
        q = np.round(audio[i] / delta)  # Lượng tử hóa
        if bit == '0':
            stego_audio[i] = delta * (2 * q)
        else:
            stego_audio[i] = delta * (2 * q + 1)
    return stego_audio

# Hàm kết hợp QIM và LSB
def combined_embed(audio_path, output_path, binary_message, delta=0.001):
    audio, sr = sf.read(audio_path, dtype='float32')
    if audio.ndim > 1:
        audio = audio[:, 0]  # Chuyển mono nếu âm thanh là stereo

    print(f"Thông điệp nhị phân dài: {len(binary_message)} bits")

    if len(binary_message) > len(audio):
        raise ValueError("Thông điệp quá dài so với file âm thanh!")

    # Nhúng thông điệp vào LSB
    stego_audio_lsb = lsb_embed(audio, binary_message[:len(audio)])

    # Nhúng phần còn lại vào QIM
    stego_audio_combined = qim_embed(stego_audio_lsb, binary_message[len(audio):], delta)

    # Ghi ra file âm thanh đã nhúng thông điệp
    sf.write(output_path, stego_audio_combined, sr)
    print(f"Đã nhúng thông điệp vào {output_path}")
    
    # Ghi chuỗi nhị phân đã nhúng vào tệp 'tepNhiPhan.txt'
    with open('tepNhiPhan.txt', 'w', encoding='utf-8') as file:
        file.write(binary_message)
    print("Đã ghi chuỗi nhị phân vào file 'tepNhiPhan.txt'")

# ==== Chạy ==== 
if __name__ == "__main__":
    input_audio = "input.wav"             # File âm thanh gốc
    output_audio = "output_audio.wav"  # File âm thanh sau khi nhúng
    message_file = "VoiVang.txt"          # File văn bản chứa thông điệp

    # Đọc văn bản từ tệp
    message = read_file(message_file)
    
    # Chuyển văn bản thành nhị phân
    binary_message = text_to_binary(message)
    
    # Ghi nhị phân vào tệp 'tepNhiPhan.txt'
    with open('tepNhiPhan.txt', 'w', encoding='utf-8') as file:
        file.write(binary_message)
    print(f"Đã xuất nhị phân vào tepNhiPhan.txt")

    # Nhúng thông điệp vào âm thanh và xuất chuỗi nhị phân đã nhúng vào tệp
    combined_embed(input_audio, output_audio, binary_message)
