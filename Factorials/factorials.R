factorial <- function(a, results=c()) {
if(a %in% results) { # If the result is provided,
    idx <- match(a, results) # Then, get the index
    return(results[idx + 1]) # And fetch the next element in the provided result vector
    }
if(a %in% c(0, 1)) { # Edge case of zero (0) or one (1)
    return(1) # 0! = 1! = 1
    }
if(a < 0) { # If the provided integer is negative,
    return("Negative integers are not allowed") # Let the user know
    } 
result <- a * factorial(a - 1) # Recursive
results <- c(results, result) # Memoize the result
return(result)
}

factorial(9)
factorial(9, c(9, 362880))