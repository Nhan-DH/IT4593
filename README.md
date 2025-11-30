Grey Wolf Optimization (GWO) – Python Implementation
Mô tả dự án

Đây là một chương trình Python triển khai thuật toán Grey Wolf Optimization (GWO), một thuật toán tối ưu hóa bầy đàn lấy cảm hứng từ hành vi săn mồi của loài sói xám. Chương trình này được thiết kế để tối ưu hóa hai hàm toán học phổ biến:

Hàm Rastrigin

𝑓
(
𝑥
)
=
∑
𝑖
=
1
𝑛
[
𝑥
𝑖
2
−
10
cos
⁡
(
2
𝜋
𝑥
𝑖
)
+
10
]
f(x)=
i=1
∑
n
	​

[x
i
2
	​

−10cos(2πx
i
	​

)+10]

Hàm này có nhiều cực trị cục bộ, thường dùng để kiểm tra khả năng tìm cực tiểu toàn cục của thuật toán.

Hàm Sphere

𝑓
(
𝑥
)
=
∑
𝑖
=
1
𝑛
𝑥
𝑖
2
f(x)=
i=1
∑
n
	​

x
i
2
	​


Hàm đơn giản, cực tiểu toàn cục tại 
𝑥
=
0
x=0.

Cách thức hoạt động

Khởi tạo: Một quần thể n sói (nghiệm) được sinh ngẫu nhiên trong miền giá trị [minx, maxx].

Cập nhật: Mỗi sói được cập nhật dựa trên 3 sói tốt nhất: alpha, beta và gamma.

Thuật toán:

Tính toán các tham số A và C giảm tuyến tính theo số vòng lặp.

Tạo nghiệm mới bằng công thức trung bình giữa alpha, beta và gamma.

Chọn lọc tham lam: nếu nghiệm mới tốt hơn, thay thế sói cũ.

Kết thúc: Sau số vòng lặp max_iter, thuật toán trả về nghiệm tốt nhất (alpha wolf).

Cấu trúc chương trình

wolf class: Đại diện cho một con sói (nghiệm), chứa vị trí và fitness.

fitness_rastrigin(position): Tính giá trị hàm Rastrigin.

fitness_sphere(position): Tính giá trị hàm Sphere.

gwo(fitness, max_iter, n, dim, minx, maxx): Thuật toán GWO chung, nhận hàm fitness và các tham số.

Tham số chính

dim: Số chiều (số biến tối ưu).

num_particles: Số lượng sói trong quần thể.

max_iter: Số vòng lặp tối đa.

minx, maxx: Giới hạn giá trị mỗi biến.

Cách chạy

Cài đặt Python 3.x.

Lưu mã nguồn vào file gwo.py.

Chạy chương trình:

python gwo.py




Giá trị fitness của giải pháp.

Thông tin quá trình tối ưu qua các vòng lặp.
