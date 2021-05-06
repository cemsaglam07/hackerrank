'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
     */
    
    /*
     * ^ => start of statement
     * () => store as capture group
     * [aeiou] => one of a,e,i,o,u
     * . => any character except line terminators
     * + => repeated 1+ times (ensures len > 3)
     * \1 => reference 1st capture group (i.e. [aeiou])
     * \\1 => first \ added for special character notation in strings
     * $ => end of statement
     */
    let re = new RegExp('^([aeiou]).+\\1$')
    
    /*
     * Do not remove the return statement
     */
    return re;
}


function main() {
    const re = regexVar();
    const s = readLine();
    
    console.log(re.test(s));
}
