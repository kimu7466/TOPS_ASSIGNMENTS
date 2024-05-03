// Q.39 Accept 3 numbers from user using while loop and check each numbers palindrome? 


// ans:


const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function isPalindrome(num) {
    const numString = num.toString();
    const reversedNumString = numString.split('').reverse().join('');
    return numString === reversedNumString;
}

let count = 0;
const numbers = [];

function getUserInput() {
    rl.question(`Enter number ${count + 1}: `, (input) => {
        const num = parseInt(input);

        if (!isNaN(num)) {
            numbers.push(num);
            count++;
        } else {
            console.log("Invalid input. Please enter a valid number.");
        }

        if (count < 3) {
            getUserInput();
        } else {
            console.log("Numbers entered:", numbers);
            checkPalindromes();
            rl.close();
        }
    });
}

function checkPalindromes() {
    numbers.forEach((num, index) => {
        if (isPalindrome(num)) {
            console.log(`Number ${index + 1} (${num}) is a palindrome.`);
        } else {
            console.log(`Number ${index + 1} (${num}) is not a palindrome.`);
        }
    });
}

console.log("Enter three numbers to check if they are palindromes:");
getUserInput();
