disp("This programs finds the nth Catalan number");
n=input("\nEnter the number : ");
disp(catalan(n))

function result = catalan(n)
    if n==0 || n==1
        result = 1;
    else
        result = fact(2*n) / (fact(n+1)*fact(n))
    end
end

function fac = fact(n)
    if n==1 || n==0 
        fac = 1;
    else
        fac = n*fact(n-1); 
    end
end