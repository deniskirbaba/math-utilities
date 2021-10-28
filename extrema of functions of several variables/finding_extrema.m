x = linspace(1.25, 2.05, 100);
y = linspace(0.85, 2, 100)';
z = x.^3 - 12.*x.*y + 8.*y.^3;

surfc(x,y,z)
hold on;
scatter3(2, 1, -8, 200, 'r', 'filled')

colormap cool;
xlabel("x");
ylabel("y");
zlabel('z');
title("x^3 - 12xy + 8y^3");

x_start = 1.3;
y_start = 1.95;
z_start = x_start.^3 - 12.*x_start.*y_start + 8.*y_start.^3;

scatter3(x_start, y_start, z_start, 50, 'black', 'filled', '*', 'DisplayName', 'minimum')
drawnow

x_prev = x_start;
y_prev = y_start;
z_prev = z_start;
x_new = x_start - step_ratio.*(3.*x_prev.^2 - 12.*y_start);
y_new = y_start - step_ratio.*(24.*y_start.^2 - 12.*x_prev);
z_new = x_new.^3 - 12.*x_new.*y_new + 8.*y_new.^3;

line_to_the_minimum = animatedline(x_start,y_start,z_start, "Color", 'r','LineWidth', 3);

step_ratio = 0.0005;
number_of_iterations = 0;
now = tic();
yintercept = 1;
subtitle(['iterations: ' int2str(number_of_iterations) ', time: ' sprintf('%.2f',toc(now)) 's, received point: (' sprintf('%.2f',x_start) ',' sprintf('%.2f',y_start) ',' sprintf('%.2f',z_start) ')'])
pause(3)
while abs(x_prev - x_new) + abs(y_prev - y_new) > 0.0001
    number_of_iterations = number_of_iterations + 1;
    x_prev = x_new;
    y_prev = y_new;
    z_prev = z_new;
    x_new = x_prev - step_ratio.*(3.*x_prev.^2 - 12.*y_prev);
    y_new = y_prev - step_ratio.*(24.*y_prev.^2 - 12.*x_prev);
    z_new = x_new.^3 - 12.*x_new.*y_new + 8.*y_new.^3;
    if isvalid(line_to_the_minimum)
        addpoints(line_to_the_minimum, x_new, y_new, z_new);
    else
        break % stop trying to add points
    end
    subtitle(['iterations: ' int2str(number_of_iterations) ', time: ' sprintf('%.2f',toc(now)) 's, received point: (' sprintf('%.2f',x_new) ',' sprintf('%.2f',y_new) ',' sprintf('%.2f',z_new) ')'])
    drawnow limitrate
    pause(0.5/number_of_iterations)
end
x_new
y_new
z_new