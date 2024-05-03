// Q.26 Write find maximum number among 3 numbers using ternary operator in JS?

// ans:


function findMax(a, b, c) {
    return a > b ? (a > c ? a : c) : (b > c ? b : c);
}

// Example usage:
console.log(findMax(5, 8, 3)); // Output: 8
