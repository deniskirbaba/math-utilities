x = linspace(-0.5, 2.5, 100); % (-0.5, 2.5, 100)
y = linspace(-0.5, 1.5, 100)'; % (-0.5, 1.5, 100)
z = x.^3 - 12.*x.*y + 8.*y.^3;

surfc(x,y,z)
hold on;
%contour3(x, y, z, [-7, -4, 0, 3], '--r', ShowText="on", LineWidth = 2)
scatter3([0, 2], [0, 1], [0, -8], 100, 'r', 'filled')
text([0, 2], [0, 1], [2, -6], ["non-extreme", "extreme"], 'FontSize', 20)
colormap cool;
xlabel("x");
ylabel("y");
zlabel('z');
title("x^3 - 12xy + 8y^3");