clc; clear; close all;

%% ==================================================
%  BÀI TOÁN TRUYỀN THÔNG
%  Tối ưu vị trí UAV Base Station bằng Grey Wolf Optimizer
%  Biến tối ưu: (x, y, h)
%% ==================================================

%% ------------------ THAM SỐ HỆ THỐNG ------------------
N_users = 20;              % số người dùng
AreaSize = 100;            % khu vực 100x100 (m)
P = 1;                     % công suất phát
path_loss = 2;             % hệ số suy hao
epsilon = 1e-3;

h_min = 10;                % độ cao UAV min (m)
h_max = 50;                % độ cao UAV max (m)

%% Vị trí người dùng ngẫu nhiên
Users = rand(N_users,2) * AreaSize;

%% ------------------ THAM SỐ GWO ------------------
SearchAgents = 30;         % số sói
MaxIter = 200;             % số vòng lặp
dim = 3;                   % (x, y, h)

lb = [0 0 h_min];
ub = [AreaSize AreaSize h_max];

%% ------------------ KHỞI TẠO ------------------
Positions = rand(SearchAgents, dim) .* (ub - lb) + lb;

Alpha_pos = zeros(1,dim);
Beta_pos  = zeros(1,dim);
Delta_pos = zeros(1,dim);

Alpha_score = inf;
Beta_score  = inf;
Delta_score = inf;

Convergence = zeros(1, MaxIter);

%% ================== VÒNG LẶP GWO ==================
for t = 1:MaxIter
    a = 2 - t * (2 / MaxIter);   % tham số giảm tuyến tính
    
    for i = 1:SearchAgents
        % Giữ nghiệm trong biên
        Positions(i,:) = max(Positions(i,:), lb);
        Positions(i,:) = min(Positions(i,:), ub);
        
        % Tính fitness
        fit = UAV_fitness(Positions(i,:), Users, P, path_loss, epsilon);
        
        % Cập nhật Alpha, Beta, Delta
        if fit < Alpha_score
            Delta_score = Beta_score;
            Delta_pos   = Beta_pos;
            
            Beta_score  = Alpha_score;
            Beta_pos    = Alpha_pos;
            
            Alpha_score = fit;
            Alpha_pos   = Positions(i,:);
            
        elseif fit < Beta_score
            Delta_score = Beta_score;
            Delta_pos   = Beta_pos;
            
            Beta_score  = fit;
            Beta_pos    = Positions(i,:);
            
        elseif fit < Delta_score
            Delta_score = fit;
            Delta_pos   = Positions(i,:);
        end
    end
    
    % Cập nhật vị trí các sói
    for i = 1:SearchAgents
        for j = 1:dim
            r1 = rand(); r2 = rand();
            A1 = 2*a*r1 - a;
            C1 = 2*r2;
            D_alpha = abs(C1*Alpha_pos(j) - Positions(i,j));
            X1 = Alpha_pos(j) - A1*D_alpha;

            r1 = rand(); r2 = rand();
            A2 = 2*a*r1 - a;
            C2 = 2*r2;
            D_beta = abs(C2*Beta_pos(j) - Positions(i,j));
            X2 = Beta_pos(j) - A2*D_beta;

            r1 = rand(); r2 = rand();
            A3 = 2*a*r1 - a;
            C3 = 2*r2;
            D_delta = abs(C3*Delta_pos(j) - Positions(i,j));
            X3 = Delta_pos(j) - A3*D_delta;

            Positions(i,j) = (X1 + X2 + X3) / 3;
        end
    end
    
    Convergence(t) = Alpha_score;
    fprintf('Iteration %d | Best Fitness = %.6f\n', t, Alpha_score);
end

%% ================== KẾT QUẢ ==================
Best_UAV = Alpha_pos;
Best_SNR = -Alpha_score;

disp('-----------------------------------');
disp('Vị trí UAV tối ưu (x, y, h):');
disp(Best_UAV);
disp('SNR trung bình tối ưu:');
disp(Best_SNR);

%% ================== VẼ KẾT QUẢ ==================
figure;
scatter(Users(:,1), Users(:,2), 50, 'b', 'filled'); hold on;
scatter(Best_UAV(1), Best_UAV(2), 150, 'r', 'filled');
legend('Users','UAV-BS');
xlabel('X'); ylabel('Y');
title('Tối ưu vị trí UAV Base Station bằng GWO');
grid on;

figure;
plot(Convergence,'LineWidth',2);
xlabel('Iteration');
ylabel('Fitness');
title('Đường hội tụ của Grey Wolf Optimizer');
grid on;

%% ==================================================
%  HÀM FITNESS (ĐẶT CUỐI FILE)
%% ==================================================
function fit = UAV_fitness(pos, Users, P, alpha, epsilon)

x = pos(1);
y = pos(2);
h = pos(3);

dist = sqrt((Users(:,1)-x).^2 + (Users(:,2)-y).^2 + h^2);
SNR = P ./ (dist.^alpha + epsilon);

fit = -mean(SNR);   % GWO là minimization

end
