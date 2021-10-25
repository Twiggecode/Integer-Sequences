% Author : Paresh Yeole
% Matlab script to determine the nth term in the alternating 
% factorial sequence

disp("This programs finds the nth term in the alternating sequence");
n=input("\nEnter the nth term whoose value you want to find");
disp(alternating_number(n+1))

function result = alternating_number(n)
    if n==0 || n==1
        result = 1;
    else
        flag = 0;
        result = 0;
        while n>0
            if flag
                result = result - fact(n);
                flag = 0;
            else
                result = result + fact(n);
                flag = 1;
            end
            n = n - 1;
        end
    end
end


function fac = fact(n)
    if n==1 || n==0 
        fac = 1;
    else
        fac = n*fact(n-1); 
    end
end