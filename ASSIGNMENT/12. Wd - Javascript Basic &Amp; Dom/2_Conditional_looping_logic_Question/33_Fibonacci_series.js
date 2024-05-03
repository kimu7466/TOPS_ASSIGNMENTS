// Q.33 Write to print Fibonacci series up to given numbers?

// ans:

function fibonacciSeries(limit) {
    let fib = [0, 1];
    for (let i = 2; i < limit; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    return fib.slice(0, limit);
}

console.log("Fibonacci series up to 10:", fibonacciSeries(10)); // Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
