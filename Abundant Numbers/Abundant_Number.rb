def get_sum_of_divisor(n)
    sum=0
    for i in 1..Math.sqrt(n)
       if n%i==0                #adds i to the sum if n is divisable by i
        sum+=i
            if n/i!=n && n/i!=i #adds n/i to the sum if result is not n or i
                sum+=n/i
            end
       end
    end
    return sum
end
def is_abundant(n)
    return get_sum_of_divisor(n)>n
    
end

if __FILE__ == $0
    num=ARGV[0].to_i
    #num=24
    count=-1
    n=12 # starting of abundant number series
    while count!=num
        if is_abundant(n)
            count+=1
        end
        n+=1
    end
        
    puts n-1
    
end