// Q.7 Check if typeof '10' is exactly equal to 10. If not make it exactly equal?


if (typeof '10' !== typeof 10) {
    const numberFromString = parseInt('10');

    if (numberFromString === 10) {
        console.log("'10' is exactly equal to 10 after conversion.");
    } else {
        console.log("'10' is not exactly equal to 10 after conversion.");
    }
} else {
    console.log("The types are already the same.");
}



