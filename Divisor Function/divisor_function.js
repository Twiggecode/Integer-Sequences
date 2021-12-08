function divisor (n) {
  if (n < 1) { 
    console.error("Invalid input, number must be more than 0");
    return [];
  } else if (n === 1) return [1];
  
  let divs = new Set(); //Instead of Array, so no duplicates can be stored
  let sqrt = Math.floor(Math.sqrt(n));

  for (let i = 1; i <= sqrt; i++) { // Only numbers less than the sqrt of "n" can be common divisors

    if (n % i === 0) {
      divs.add(i);
      if (n / (i % 1) !== 0) { // If the current iteration can divide "n" (and NOT return a number with decimals), the result is another common divisor
        divs.add(n / i);
      }
    }
  }; // End of Loop
    
  return Array.from(divs).sort( (a, b) => a - b); // Turn back into array, sort it by lowest-to-highest number
};
