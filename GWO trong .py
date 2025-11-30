# triển khai thuật toán Grey Wolf Optimization (GWO) bằng Python
# tối ưu hóa hàm Rastrigin và Sphere

import random
import math    # dùng cos() cho hàm Rastrigin
import copy    # để copy mảng tiện lợi
import sys     # dùng max float nếu cần

#-------hàm fitness---------

# hàm Rastrigin
def fitness_rastrigin(position):
    fitness_value = 0.0
    for i in range(len(position)):
        xi = position[i]
        fitness_value += (xi * xi) - (10 * math.cos(2 * math.pi * xi)) + 10
    return fitness_value

# hàm Sphere
def fitness_sphere(position):
    fitness_value = 0.0
    for i in range(len(position)):
        xi = position[i]
        fitness_value += (xi*xi)
    return fitness_value

#-------------------------

# lớp sói
class wolf:
    def __init__(self, fitness, dim, minx, maxx, seed):
        self.rnd = random.Random(seed)
        self.position = [0.0 for i in range(dim)]

        # khởi tạo vị trí ngẫu nhiên trong khoảng minx → maxx
        for i in range(dim):
            self.position[i] = ((maxx - minx) * self.rnd.random() + minx)

        # tính giá trị fitness ban đầu
        self.fitness = fitness(self.position)

#-------------------------

# thuật toán GWO
def gwo(fitness, max_iter, n, dim, minx, maxx):
    rnd = random.Random(0)

    # tạo n con sói ngẫu nhiên
    population = [ wolf(fitness, dim, minx, maxx, i) for i in range(n)]

    # sắp xếp theo giá trị fitness tăng dần
    population = sorted(population, key = lambda temp: temp.fitness)

    # 3 sói tốt nhất: alpha, beta, gamma
    alpha_wolf, beta_wolf, gamma_wolf = copy.copy(population[:3])

    # vòng lặp chính
    Iter = 0
    while Iter < max_iter:

        # in kết quả sau mỗi 10 vòng lặp
        if Iter % 10 == 0 and Iter > 1:
            print("Vòng = " + str(Iter) + " giá trị fitness tốt nhất = %.3f" % alpha_wolf.fitness)

        # a giảm dần từ 2 → 0
        a = 2*(1 - Iter/max_iter)

        # cập nhật vị trí mỗi con sói dựa trên alpha, beta, gamma
        for i in range(n):
            A1, A2, A3 = a * (2 * rnd.random() - 1), a * (2 * rnd.random() - 1), a * (2 * rnd.random() - 1)
            C1, C2, C3 = 2 * rnd.random(), 2*rnd.random(), 2*rnd.random()

            X1 = [0.0 for i in range(dim)]
            X2 = [0.0 for i in range(dim)]
            X3 = [0.0 for i in range(dim)]
            Xnew = [0.0 for i in range(dim)]

            for j in range(dim):
                X1[j] = alpha_wolf.position[j] - A1 * abs(C1 * alpha_wolf.position[j] - population[i].position[j])
                X2[j] = beta_wolf.position[j] - A2 * abs(C2 * beta_wolf.position[j] - population[i].position[j])
                X3[j] = gamma_wolf.position[j] - A3 * abs(C3 * gamma_wolf.position[j] - population[i].position[j])
                Xnew[j] += X1[j] + X2[j] + X3[j]

            # tính trung bình 3 hướng
            for j in range(dim):
                Xnew[j] /= 3.0

            # tính fitness vị trí mới
            fnew = fitness(Xnew)

            # chọn vị trí tốt hơn
            if fnew < population[i].fitness:
                population[i].position = Xnew
                population[i].fitness = fnew

        # sắp xếp lại và chọn alpha, beta, gamma mới
        population = sorted(population, key = lambda temp: temp.fitness)
        alpha_wolf, beta_wolf, gamma_wolf = copy.copy(population[:3])

        Iter += 1

    # trả về vị trí của sói tốt nhất
    return alpha_wolf.position

#-------------------------

# chạy GWO với hàm Rastrigin
print("\nBắt đầu tối ưu Grey Wolf trên hàm Rastrigin\n")
dim = 3
fitness = fitness_rastrigin

print("Mục tiêu: giảm giá trị hàm Rastrigin với " + str(dim) + " biến")
print("Hàm có giá trị min = 0.0 tại (", end="")
for i in range(dim-1):
    print("0, ", end="")
print("0)")

num_particles = 50
max_iter = 100

print("Số sói = " + str(num_particles))
print("Số vòng lặp = " + str(max_iter))
print("\nBắt đầu thuật toán GWO\n")

best_position = gwo(fitness, max_iter, num_particles, dim, -10.0, 10.0)

print("\nGWO hoàn tất\n")
print("Vị trí tốt nhất tìm được:")
print(["%.6f"%best_position[k] for k in range(dim)])
err = fitness(best_position)
print("Giá trị fitness của vị trí tốt nhất = %.6f" % err)
print("\nKết thúc GWO trên hàm Rastrigin\n")

#-------------------------

# chạy GWO với hàm Sphere
print("\nBắt đầu tối ưu Grey Wolf trên hàm Sphere\n")
dim = 3
fitness = fitness_sphere

print("Mục tiêu: giảm giá trị hàm Sphere với " + str(dim) + " biến")
print("Hàm có giá trị min = 0.0 tại (", end="")
for i in range(dim-1):
    print("0, ", end="")
print("0)")

num_particles = 50
max_iter = 100

print("Số sói = " + str(num_particles))
print("Số vòng lặp = " + str(max_iter))
print("\nBắt đầu thuật toán GWO\n")

best_position = gwo(fitness, max_iter, num_particles, dim, -10.0, 10.0)

print("\nGWO hoàn tất\n")
print("Vị trí tốt nhất tìm được:")
print(["%.6f"%best_position[k] for k in range(dim)])
err = fitness(best_position)
print("Giá trị fitness của vị trí tốt nhất = %.6f" % err)
print("\nKết thúc GWO trên hàm Sphere\n")
