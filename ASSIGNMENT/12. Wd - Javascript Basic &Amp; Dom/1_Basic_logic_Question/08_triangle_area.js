// Q.8 Write a JavaScript Program to find the area of a triangle? 

// ans:


function calculateTriangleArea(base, height) {
    const area = 0.5 * base * height;
    return area;
}

const base = 5;
const height = 8;
const area = calculateTriangleArea(base, height);
console.log("The area of the triangle with base", base, "and height", height, "is:", area);
