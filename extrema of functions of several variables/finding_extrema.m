% initialization part
% definition of the functions defining the surface is in the file "func.m"
% if u want to change surface, change the function ("func.m" file) and
% derivatives ("z_der_x.m" and "z_der_x.m" files)

function_title = "x^3 - 12xy + 8y^3";   % this will be displayed in the title of the graph
x_boundary = [1.25 2.05];       % oX displayed surface boundaries
y_boundary = [0.85 2];          % oY displayed surface boundaries
number_of_dots_in_x_boundary = 100;
number_of_dots_in_y_boundary = 100;
minimum = [2 1 -8];       % coordinates of the investigated minimum point
starting_point = [1.3 1.95 func(1.3, 1.95)];    % coordinates of the starting point
step_ratio = 0.005;     % this coefficient is responsible for the rate of step decrease
pause_flag = true;      % if true, then adds pauses when building a graph for a more visual work of the program
shutdown_criterion_value = 0.0001;  % 

% executing part

x = linspace(x_boundary(1), x_boundary(2), number_of_dots_in_x_boundary);
y = linspace(y_boundary(1), y_boundary(2), number_of_dots_in_y_boundary)';

surfc(x,y,func(x, y))
hold on;
scatter3(minimum(1), minimum(2), minimum(3), 200, 'r', 'filled')

colormap cool;
xlabel("x");
ylabel("y");
zlabel('z');
title(function_title);

scatter3(starting_point(1), starting_point(2), starting_point(3), 50, 'black', 'filled', '*', 'DisplayName', 'minimum')
drawnow

x_prev = starting_point(1);
y_prev = starting_point(2);
z_prev = starting_point(3);
x_new = starting_point(1) - step_ratio.*z_der_x(x_prev, y_prev);
y_new = starting_point(2) - step_ratio.*z_der_y(x_prev, y_prev);
z_new = func(x_new, y_new);

line_to_the_minimum = animatedline(starting_point(1),starting_point(2),starting_point(3), "Color", 'r','LineWidth', 3);

number_of_iterations = 0;
now = tic();
subtitle(['iterations: ' int2str(number_of_iterations) ', time: ' sprintf('%.2f',toc(now)) 's, received point: (' sprintf('%.2f',x_start) ',' sprintf('%.2f',y_start) ',' sprintf('%.2f',z_start) ')'])

if (pause_flag)
    pause(3)
end

while abs(x_prev - x_new) + abs(y_prev - y_new) > shutdown_criterion_value
    number_of_iterations = number_of_iterations + 1;
    x_prev = x_new;
    y_prev = y_new;
    z_prev = z_new;
    x_new = x_prev - step_ratio.*z_der_x(x_prev, y_prev);
    y_new = y_prev - step_ratio.*z_der_y(x_prev, y_prev);
    z_new = func(x_new, y_new);
    if isvalid(line_to_the_minimum)
        addpoints(line_to_the_minimum, x_new, y_new, z_new);
    else
        break % stop trying to add points
    end
    subtitle(['iterations: ' int2str(number_of_iterations) ', time: ' sprintf('%.2f',toc(now)) 's, received point: (' sprintf('%.2f',x_new) ',' sprintf('%.2f',y_new) ',' sprintf('%.2f',z_new) ')'])
    drawnow limitrate
    
    if (pause_flag)
        pause(0.5/number_of_iterations)
    end
end