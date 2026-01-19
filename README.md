UAV Base Station Optimization using Grey Wolf Optimizer (GWO)
1. Giới thiệu

Dự án này mô phỏng bài toán tối ưu vị trí UAV Base Station trong mạng truyền thông không dây bằng thuật toán Grey Wolf Optimizer (GWO).

Mục tiêu là tìm vị trí tối ưu của UAV trong không gian 3D (x, y, h) để tối đa hóa SNR trung bình của các người dùng trên mặt đất.

2. Mô hình hệ thống
2.1 Người dùng

Số lượng: 20

Phân bố ngẫu nhiên trong khu vực 100m × 100m

2.2 UAV Base Station

Biến tối ưu:

x, y: tọa độ mặt phẳng

h: độ cao UAV

Giới hạn:
h_min = 10
h_max = 50

2.3 Mô hình kênh

SNR của mỗi user được tính theo công thức:

SNR = P / (d^α + ε)

Trong đó:

P = 1: công suất phát

α = 2: hệ số suy hao

ε = 10^-3: tránh chia cho 0

d: khoảng cách từ UAV đến user

2.4 Hàm mục tiêu

Tối đa hóa SNR trung bình:

SNR_avg = (1/N) * Σ SNR_i

Do GWO là bài toán minimization, ta dùng:

fit = -mean(SNR)

3. Thuật toán Grey Wolf Optimizer (GWO)
3.1 Tham số

Số sói: 30

Số vòng lặp: 200

Số chiều: 3

3.2 Các cá thể lãnh đạo

Alpha: nghiệm tốt nhất

Beta: nghiệm tốt thứ hai

Delta: nghiệm tốt thứ ba

Các sói còn lại cập nhật vị trí dựa trên ba cá thể này.

4. Cấu trúc chương trình

main.m
README.md

File main.m gồm:

Khởi tạo tham số hệ thống

Sinh vị trí người dùng

Khởi tạo GWO

Vòng lặp tối ưu

Hiển thị kết quả

Vẽ đồ thị

Hàm fitness

5. Kết quả đầu ra

Chương trình hiển thị:

Vị trí UAV tối ưu (x, y, h)

SNR trung bình tối ưu

Ngoài ra còn có:

Hình vị trí UAV và người dùng

Đồ thị hội tụ của GWO

6. Cách chạy chương trình

Bước 1: Mở MATLAB

Bước 2: Chuyển thư mục:

cd path_to_project

Bước 3: Chạy chương trình:

main

7. Hướng mở rộng

Thêm nhiễu AWGN

Mô hình LOS/NLOS

Nhiều UAV

So sánh với PSO hoặc GA

Tối ưu theo throughput
