
// rotateString(str, amount)
// returns a copy of the given string (str) rotated to the right a number
// (amount) of characters - i.e. the string is shifted to the right that
// number of characters, and anything that would go past the end of the string
// returns to the front
//
// rotateString("Good morning!", 3) -> "ng!Good morni"
// rotateString("Good morning!", 4) -> "ing!Good morn"
// rotateString("Good morning!", 5) -> "ning!Good mor"
//
// the output string length should be exactly the same as the input string length
//
// remember that strings are immutable - you're going to have to create a
// new string
//
// bonus objectives if u wanna: can the amount be more than the string length?
// what if amount is negative? can you rotate it to the left?

    // put code here
    // return a new string as your output
}


// should return "abases!Let's talk about relational dat"

// should return "abcde"

// isRotation(stringA, stringB)
// returns true if a rotation of stringA could form stringB or vice versa
// (if one is true, the other is true)
// return false otherwise
//
// isRotation("Good morning!", "ng!Good morni") -> true
// isRotation("Good morning!", "ng! Good morni") -> false
// (the strings are of different lengths, it's not possible)
// isRotation("Good morning!", "ng!Good monri") -> false
//
// suggestion - this is brute forceable, but once you get that working
// see if there's a more elegant solution for a more civilized age

// function isRotation(stringA, stringB) {
    // put code here


// come up with your own test cases for this one!
// they won't always be given to you in the real world


function rotateString(str, amount)
{
    
    result = "";
    for(var i = str.length - amount;i < str.length; i++)
    {
        result = result + str[i];
    }
    for(var i = 0;i < str.length - amount; i++)
    {
        result=result+str[i];
    }
    return result
}

console.log(rotateString("Good morning!", 3));
console.log(rotateString("abcde", 5))
console.log(rotateString("Let's talk about relational databases!", 7))

function isRotation(stringA, stringB)
{

    if(stringA.length != stringB.length)
    {
        return false;
    }

    result = "";
    for(var i = 0;i < stringA.length; i++)
    {
        
        result = rotateString(stringA, i)
        if(result === stringB)
        {
            return true;
        }
    }
    return false;
}



// isRotation("Good morning!", "ng!Good morni") -> true
// isRotation("Good morning!", "ng! Good morni") -> false
// (the strings are of different lengths, it's not possible)
// isRotation("Good morning!", "ng!Good monri") -> false

console.log(isRotation("Good morning!", "ng!Good morni"));
console.log(isRotation("Good morning!", "ng! Good morni"));
console.log(isRotation("Good morning!", "ng!Good monri"));

