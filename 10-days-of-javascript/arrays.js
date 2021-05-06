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

/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // ... is the "spread" syntax equivalent to *values in Python
    let biggestNum = Math.max(...nums);
    // Remove numbers with biggest values
    while (true) {
        let index = nums.indexOf(biggestNum);
        if (index > -1) {
            nums.splice(index, 1);
            continue;
        }
        break;
    }
    // Return (the second) biggest number
    return Math.max(...nums);
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}
