// Q.12 WAP to convert years into days and days into years? 


// // ans:

function yearsToDays(years) {

    const days = years * 365;
    return days;
}

const years = 3;
const days = yearsToDays(years);
console.log(years + " years is equal to " + days + " days.");



function daysToYears(days_) {

    const years_ = days_ / 365;
    return years_;
}


const days_ = 1095; 
const years_ = daysToYears(days_);
console.log(days_ + " days is equal to " + years_ + " years.");





