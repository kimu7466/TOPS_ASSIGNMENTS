// Q.38 Use pattern in console.log in JS?

// 1
// 1 0
// 1 0 1
// 1 0 1 0
// 1 0 1 0 1 

// ans:

const numRows = 5;

for (let i = 1; i <= numRows; i++) {
    let row = "";
    
    for (let j = 1; j <= i; j++) {
        const value = j % 2 === 0 ? "0" : "1";
        
        row += value + " ";
    }
    
    console.log(row);
}




