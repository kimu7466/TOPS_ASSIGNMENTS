// Q.13 Convert temperature Fahrenheit to Celsius? (Conditional logic Question)


// ans:


function fahrenheitToCelsius(fahrenheit) {
    const celsius = (fahrenheit - 32) * 5 / 9;
    return celsius;
}

// Example usage:
const fahrenheit = 100;
const celsius = fahrenheitToCelsius(fahrenheit);
console.log(fahrenheit + " degrees Fahrenheit is equal to " + celsius + " degrees Celsius.");
