# Grey Wolf Optimization (GWO) – Triển khai bằng Python

## Mô tả dự án

Đây là chương trình Python triển khai thuật toán **Grey Wolf Optimization (GWO)**, một thuật toán tối ưu hóa bầy đàn lấy cảm hứng từ hành vi săn mồi của loài sói xám. Chương trình tối ưu hóa hai hàm toán học phổ biến:

1. **Hàm Rastrigin**  
   \[
   f(x) = \sum_{i=1}^{n} [x_i^2 - 10 \cos(2 \pi x_i) + 10]
   \]  
   Hàm này có nhiều cực trị cục bộ, dùng để kiểm tra khả năng tìm cực tiểu toàn cục của thuật toán.

2. **Hàm Sphere**  
   \[
   f(x) = \sum_{i=1}^{n} x_i^2
   \]  
   Hàm đơn giản, cực tiểu toàn cục tại \(x = 0\).

## Cách thức hoạt động

- **Khởi tạo**: Một quần thể `n` sói (nghiệm) được sinh ngẫu nhiên trong miền `[minx, maxx]`.
- **Cập nhật**: Mỗi sói được cập nhật dựa trên 3 sói tốt nhất: **alpha**, **beta**, **gamma**.
- **Thuật toán**:  
  - Tính tham số `A` và `C` giảm tuyến tính theo số vòng lặp.  
  - Tạo nghiệm mới bằng trung bình giữa alpha, beta và gamma.  
  - Chọn lọc tham lam: nếu nghiệm mới tốt hơn, thay thế sói cũ.
- **Kết thúc**: Sau số vòng lặp `max_iter`, thuật toán trả về nghiệm tốt nhất (alpha wolf).

## Cấu trúc chương trình

- `wolf` class: Đại diện cho một con sói (nghiệm), chứa vị trí và fitness.  
- `fitness_rastrigin(position)`: Tính giá trị hàm Rastrigin.  
- `fitness_sphere(position)`: Tính giá trị hàm Sphere.  
- `gwo(fitness, max_iter, n, dim, minx, maxx)`: Thuật toán GWO chung, nhận hàm fitness và các tham số.

## Tham số chính

- `dim`: Số chiều (số biến tối ưu).  
- `num_particles`: Số lượng sói trong quần thể.  
- `max_iter`: Số vòng lặp tối đa.  
- `minx`, `maxx`: Giới hạn giá trị mỗi biến.

## Cách chạy

1. Cài đặt Python 3.x.  
2. Lưu mã nguồn vào file `gwo.py`.  
3. Chạy chương trình:
```bash
python gwo.py
