// Q.35 Write a program make a summation of given number (E.g., 1523 Ans: - 11) in JS? 

// ans:


function digitSum(number) {

    const numberString = number.toString();
    
    let sum = 0;

    for (let i = 0; i < numberString.length; i++) {

        sum += parseInt(numberString[i]);
    }
    
    return sum;
}


const number = 1523;
const sum = digitSum(number);
console.log("Sum of digits of", number, "is:", sum);
