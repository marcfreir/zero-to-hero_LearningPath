/*
    Created on : 13-Jun-2020, 10:54:08 AM
    Author     : Marc Freir
    License    : This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
*/

'use strict'

//Make shure the page is completely loaded
window.addEventListener('load', () => {
    console.log('page is fully loaded');
    //evaluateAandBIsEqualOrGreaterOrLessThan();
    evalAandB();
    printDaysOfTheWeek();
});

//Just a test with equality/inequality operation - validation
//GLOBALS
let a = 4;
let b = 5;

/*
if (a > b) {
    console.log(`${a} is greater than ${b}`);
} else {
    if (a < b) {
        console.log(`${a} is less than ${b}`);
    } else {
        if (a === b) {
            console.log(`${a} is equal to ${b}`);
        } else {
            console.log(`Error: ${a} or ${b} are not valid numbers!`);
        }
    }
}
*/

//Encapsulating everything the inequality test inside a function:
function evaluateAandBIsEqualOrGreaterOrLessThan() {
    if (a > b) {
        console.log(`${a} is greater than ${b}`);
    } else {
        if (a < b) {
            console.log(`${a} is less than ${b}`);
        } else {
            if (a === b) {
                console.log(`${a} is equal to ${b}`);
            } else {
                console.log(`Error: ${a} or ${b} are not valid numbers!`);
            }
        }
    }
}

//Lets try with a arrow function - for short let's call the function evalAandB
const evalAandB = () => {
    if (a > b) {
        console.log(`${a} is greater than ${b}`);
    } else {
        if (a < b) {
            console.log(`${a} is less than ${b}`);
        } else {
            if (a === b) {
                console.log(`${a} is equal to ${b}`);
            } else {
                console.log(`Error: ${a} or ${b} are not valid numbers!`);
            }
        }
    }
}

const newLocal = 6;
//Now let's try the Days of The Week
let day = newLocal;

if (day === 1) {
    console.log(`The ${day}º is Sunday`);
} else {
    if (day === 2) {
        console.log(`The ${day}º is Monday`);
    } else {
        if (day === 3) {
            console.log(`The ${day}º is Tuesday`);
        } else {
            if (day === 4) {
                console.log(`The ${day}º is Wednesday`);
            } else {
                if (day === 5) {
                    console.log(`The ${day}º is Thursday`);
                } else {
                    if (day === 6) {
                        console.log(`The ${day}º is Friday`);
                    } else {
                        if (day === 7) {
                            console.log(`The ${day}º is Saturday`);
                        }
                        else {
                            console.log(`Error: ${day} isn't a valid day...`);
                        }
                    }
                }
            }
        }
    }
}

//Encapsulating everything the inequality test inside a function with CASE STATEMENT:
const printDaysOfTheWeek = () => {
    //console.log(`The ${day}º is Sunday`);
    let dayAnswer = '';
    switch (day) {
        case 1: dayAnswer = `Sunday`;
        break;
        case 2: dayAnswer = `Monday`;
        break;
        case 3: dayAnswer = `Tuesday`;
        break;
        case 4: dayAnswer = `Wednesday`;
        break;
        case 5: dayAnswer = `Thursday`;
        break;
        case 6: dayAnswer = `Friday`;
        break;
        case 7: dayAnswer = `Saturday`;
        break;
    }
    console.log(`The ${day}º is ${dayAnswer}`);
}