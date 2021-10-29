% function necessary for the program to work, 
% if to change a function it is necessary to manually write both a new function and its derivatives

% surface defining function
function z = func(x, y)            
    z = x.^3 - 12.*x.*y + 8.*y.^3;
end