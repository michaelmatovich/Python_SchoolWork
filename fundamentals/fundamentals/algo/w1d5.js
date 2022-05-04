const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
  abc: 42,
  3: "wassup",
  yo: true,
};

const keys2 = [];
const vals2 = [];
const expected2 = {};

/**
#  * Converts the given arrays of keys and values into an object.
#  * - Time: O(?).
#  * - Space: O(?).
#  * @param {Array<string>} keys
#  * @param {Array<any>} values
#  * @returns {Object} The object with the given keys and values.
#  */
function zipArraysIntoMap(keys, values) 
{
    var x = keys;
    var y = values;
    var z = x.map(function(e, i) {
        return [e, y[i]];
    });
    console.log(z);

}


/*************************************/

/* 
#   Invert Hash
#   A hash table / hash map is an obj / dictionary
#   Given an object / dict,
#   return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
# */

const obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

/**
#  * Inverts the given object's key value pairs so that the original values
#  * become the keys and the original keys become the values.
#  * - Time: O(?).
#  * - Space: O(?).
#  * @param {Object<string, any>} obj
#  * @return The given object with key value pairs inverted.
#  */
function invertObj(obj) {}


// Given a dollar amount with change (an integer w/decimal) convert to change. Make sure to count the largest denomination first!

 // Example: 3.21 --> 12 quarters, 2 dimes, 1 penny

var input = 3.21;
function generateCoinChange(input) {
    var x = input *100;
    var quarters = Math.floor(x/25);
    var dimes = Math.floor((x-(quarters * 25))/10);
    var nickles = Math.floor((x-(quarters * 25) - (dimes * 10))/5);
    var pennies = x-(quarters * 25) - (dimes * 10) - (nickles * 5)

    var result = quarters + "-" + dimes + '-' + nickles + '-' + pennies;
    return result;
}

console.log(generateCoinChange(input));



