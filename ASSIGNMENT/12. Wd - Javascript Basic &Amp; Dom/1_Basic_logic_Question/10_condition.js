// Q.10 What is Condition Statement? 


// ans:

// A condition statement, also known as a conditional statement or conditional expression, is a programming construct that allows you to execute different blocks of code based on whether a specified condition evaluates to true or false.

// In JavaScript, as in many other programming languages, the primary conditional statement is the `if` statement. Here's a basic example:

let temperature = 25;

if (temperature > 30) {
    console.log("It's a hot day!");
} else {
    console.log("It's not too hot today.");
}

// In this example, the `if` statement checks if the `temperature` variable is greater than 30. If the condition is true, it executes the code block inside the curly braces following the `if` statement. If the condition is false, it skips that block and moves to the `else` block (if provided), executing its code block instead.

// JavaScript also supports additional conditional constructs like `else if` and the ternary operator (`? :`), which allow for more complex branching logic. 

let hour = 10;
let greeting;

if (hour < 12) {
    greeting = "Good morning!";
} else if (hour >= 12 && hour < 18) {
    greeting = "Good afternoon!";
} else {
    greeting = "Good evening!";
}

console.log(greeting);

// Here, depending on the value of `hour`, different greetings are assigned to the `greeting` variable.

// Conditional statements are fundamental to programming because they allow for the creation of flexible and dynamic code that can respond to different situations or inputs.