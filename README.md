# Demo_QIM_LSB


# Dự án Giấu Thông Điệp vào Âm Thanh

## Mô tả
Dự án này sử dụng phương pháp **QIM (Quantization Index Modulation)** kết hợp với **LSB (Least Significant Bit)** để giấu thông điệp vào tệp âm thanh. Thông điệp có thể là văn bản và sẽ được chuyển thành nhị phân trước khi nhúng vào các mẫu âm thanh của tệp âm thanh gốc. Tệp âm thanh đã giấu tin có thể được lưu lại và sau đó có thể truy xuất thông điệp đã giấu bằng cách sử dụng các phương pháp ngược lại.

## Các Tệp trong Dự án

1. **`QIM_LSB.py`**: 
   - Đây là tệp chứa mã Python để nhúng thông điệp vào âm thanh. Sử dụng các phương pháp **LSB** và **QIM** để giấu thông điệp vào tệp âm thanh.
   - Tệp này thực hiện các bước sau:
     - Chuyển đổi thông điệp văn bản thành nhị phân.
     - Nhúng thông điệp vào âm thanh sử dụng **LSB** và **QIM**.
     - Lưu tệp âm thanh mới đã giấu tin và xuất chuỗi nhị phân vào một tệp.

2. **`check.py`**:
   - Tệp này được sử dụng để kiểm tra sự khác biệt giữa tệp âm thanh gốc và tệp âm thanh đã giấu thông điệp. 
   - Mã trong tệp này vẽ đồ thị cho tín hiệu âm thanh gốc và tín hiệu đã giấu tin, với các điểm thay đổi được hiển thị bằng màu đỏ.

3. **`VoiVang.txt`**:
   - Đây là tệp văn bản chứa thông điệp cần giấu vào tệp âm thanh. Dự án sử dụng văn bản này để chuyển thành nhị phân và giấu vào âm thanh.

4. **`tepNhiPhan.txt`**:
   - Tệp này chứa thông điệp đã được chuyển thành chuỗi nhị phân để giấu vào tệp âm thanh.

5. **`input.wav`** và **`output_audio.wav`**:
   - **`input.wav`** là tệp âm thanh gốc, trong đó thông điệp sẽ được giấu.
   - **`output_audio.wav`** là tệp âm thanh mới sau khi thông điệp đã được giấu vào.

## Cài Đặt

Để chạy dự án này, bạn cần cài đặt các thư viện Python sau:

```bash
pip install librosa numpy soundfile matplotlib
