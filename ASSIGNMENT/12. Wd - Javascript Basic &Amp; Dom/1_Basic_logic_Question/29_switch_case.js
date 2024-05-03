// Q.29 Write to show
// i. Monday to Sunday using switch case in JS?
// ii. Vowel or Consonant using switch case in JS?


// ans:


function getDayName(day) {
    let dayName;
    switch (day) {
        case 1:
            dayName = "Monday";
            break;
        case 2:
            dayName = "Tuesday";
            break;
        case 3:
            dayName = "Wednesday";
            break;
        case 4:
            dayName = "Thursday";
            break;
        case 5:
            dayName = "Friday";
            break;
        case 6:
            dayName = "Saturday";
            break;
        case 7:
            dayName = "Sunday";
            break;
        default:
            dayName = "Invalid day";
    }
    return dayName;
}


for (let i = 1; i <= 7; i++) {
    console.log("Day " + i + ": " + getDayName(i));
}


function checkLetterType(letter) {
    letter = letter.toLowerCase();
    let result;
    switch (letter) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            result = "Vowel";
            break;
        default:
            result = "Consonant";
    }
    return result;
}


console.log("A is a " + checkLetterType('A'));
console.log("B is a " + checkLetterType('B'));



