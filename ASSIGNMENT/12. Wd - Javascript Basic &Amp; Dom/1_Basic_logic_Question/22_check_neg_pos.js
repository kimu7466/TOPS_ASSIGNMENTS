// Q.22 Check Number Is Positive or Negative in JavaScript?

// ans:


function checkNumberSign(num) {
    if (num > 0) {
        return "Positive";
    } else if (num < 0) {
        return "Negative";
    } else {
        return "Zero";
    }
}

// Example usage:
console.log(checkNumberSign(5)); // Output: "Positive"
console.log(checkNumberSign(-5)); // Output: "Negative"
console.log(checkNumberSign(0)); // Output: "Zero"
