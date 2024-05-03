// Q.34 Write to print number in reverse order e.g.: number = 64728 ---> reverse =82746 in JS? 

// ans:


function reverseNumber(number) {

    const numberString = number.toString();
    
    const reversedString = numberString.split('').reverse().join('');
    
    const reversedNumber = parseInt(reversedString);
    
    return reversedNumber;
}


const number = 64728;
const r_Number = reverseNumber(number);
console.log("Original number:", number);
console.log("Reversed number:", r_Number);
