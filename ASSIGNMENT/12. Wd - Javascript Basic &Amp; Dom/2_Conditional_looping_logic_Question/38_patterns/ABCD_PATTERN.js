// A
// B C
// D E F
// G H I J
// K L M N O

const numRows = 5;

let currentCharCode = 65; 

for (let i = 1; i <= numRows; i++) {
    let row = "";
    
    for (let j = 1; j <= i; j++) {
        row += String.fromCharCode(currentCharCode) + " ";
        
        currentCharCode++;
    }    
    console.log(row);
}
