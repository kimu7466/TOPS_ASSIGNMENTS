// Q.32 Write to print factorial of given number?

// ans:


function factorial(n) {
    if (n === 0 || n === 1) {
        return 1;
    }
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
let n = 5
console.log(`Factorial of ${n}: `, factorial(n)); // Output: 120
