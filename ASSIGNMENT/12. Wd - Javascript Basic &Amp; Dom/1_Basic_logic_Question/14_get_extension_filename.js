// Q.14 Write a JavaScript exercise to get the extension of a filename.?


// ans:


function getFileExtension(filename) {
    return filename.split('.').pop();
}

const filename = "example.html";
const extension = getFileExtension(filename);
console.log("The extension of the filename '" + filename + "' is '" + extension + "'.");
