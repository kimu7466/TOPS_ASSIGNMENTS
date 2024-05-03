// Q.9 Write a JavaScript program to calculate days left until next Christmas? 

// ans:

function daysUntilNextChristmas() {
    
    const currentDate = new Date();

    const currentYear = currentDate.getFullYear();
    
    const targetDate = new Date(currentYear, 11, 25); 
    
    if (currentDate > targetDate) {
        
        targetDate.setFullYear(currentYear + 1);
    }
    
    const differenceInMilliseconds = targetDate - currentDate;
    
    const daysLeft = Math.ceil(differenceInMilliseconds / (1000 * 60 * 60 * 24));

    return daysLeft;
}

const daysLeft = daysUntilNextChristmas();
console.log("Days left until next Christmas:", daysLeft);
