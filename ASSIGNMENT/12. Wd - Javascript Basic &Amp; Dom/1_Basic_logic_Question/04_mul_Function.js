// Q.4 Write a mul Function Which will Work Properly When invoked With Following Syntax.

// ans:

function mul(...args) {
    if (args.length === 0) {
        return 0; 
    } else if (args.length === 1) {
        return args[0]; 
    } else {
        
        return args.reduce((accumulator, currentValue) => accumulator * currentValue);
    }
}


console.log(mul()); 
console.log(mul(5)); 
console.log(mul(2, 3)); 
console.log(mul(2, 3, 4)); 
console.log(mul(2, 3, 4, 5)); 
