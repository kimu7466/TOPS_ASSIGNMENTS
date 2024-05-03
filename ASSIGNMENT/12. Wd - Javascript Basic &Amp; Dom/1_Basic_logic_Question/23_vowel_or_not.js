// Q.23 Find the Character Is Vowel or Not ?

// ans:


function isVowel(char) {
    char = char.toLowerCase();
    return ['a', 'e', 'i', 'o', 'u'].includes(char);
}

// Example usage:
console.log(isVowel('A')); // Output: true
console.log(isVowel('b')); // Output: false
