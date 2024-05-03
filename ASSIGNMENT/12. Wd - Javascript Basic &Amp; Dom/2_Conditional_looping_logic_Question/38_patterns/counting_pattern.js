// 1
// 2 3
// 4 5 6
// 7 8 9 10
// 11 12 13 14 15


const numRows = 5;
let counter = 1;

for (let i = 1; i <= numRows; i++) {
    let row = "";
    
    for (let j = 1; j <= i; j++) {
        row += counter + " ";
        counter++;
    }
    
    console.log(row);
}
