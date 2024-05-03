// Q.11 Find circumference of Rectangle formula : C = 4 * a ? 

// ans:

function calculateRectangleCircumference(length, width) {
    const circumference = 2 * (length + width);
    return circumference;
}

const length = 5;
const width = 3;
const circumference = calculateRectangleCircumference(length, width);
console.log("The circumference of the rectangle with length", length, "and width", width, "is:", circumference);
