// Q.19 What is the use of isNaN function?

// ans:

// The isNaN() function is used to determine whether a value is NaN (Not-a-Number) or not. 
// It returns true if the value is NaN, and false if it is a valid number or can be converted to one.



// Perform a mathematical operation resulting in NaN
let result = 0 / 0;
console.log("Result:", result); // Output: NaN

// Check if a value is NaN
let value = NaN;
if (isNaN(value)) {
  console.log("The value is NaN");
} else {
  console.log("The value is not NaN");
}
