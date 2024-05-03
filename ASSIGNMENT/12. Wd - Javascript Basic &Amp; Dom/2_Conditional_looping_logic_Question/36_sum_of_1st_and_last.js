// Q.36 Write a program you have to make a summation of first and last Digit. (E.g., 1234 Ans:- 5) in JS? 


// ans:

function sumFirstAndLastDigits(number) {

    const numberString = number.toString();
    
    const firstDigit = parseInt(numberString[0]);
    const lastDigit = parseInt(numberString[numberString.length - 1]);
    
    const sum = firstDigit + lastDigit;
    
    return sum;
}

// Example usage:
const number = 1234;
const sum = sumFirstAndLastDigits(number);
console.log("Sum of first and last digits of", number, "is:", sum);


