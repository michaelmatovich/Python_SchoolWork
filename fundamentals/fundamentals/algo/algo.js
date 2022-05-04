// parensValid(input)
// input is a string
// return true if the input has a valid configuration of parentheses and false
// otherwise. by "return true/false" I mean the boolean value, not a string
// what's valid?
// - no more open parens than close parens or vice versa
// - no close parens that appear before a valid open paren
// - ignore all other characters that are not ( and )
// - () -> true
// - )( -> false
// - hello! -> true (???)
// - (()) -> true
// - (q(a)(x)(!(7(xx)(34)(2, 7, 11)))) -> true
// - (() -> false
// - hello!() -> true
// suggestion - don't bother trying to split the string...
// it won't do us any good and just makes things more complicated
// suggestion again - do we have to check every single character in the input?
// hypothetical input: ) followed by one billion characters
// or: a) followed by one billion characters
// or: a37()) followed by one billion characters

function parensValid(str) {
    
    var left = 0;
    var right = 0;
    for (var i = 0; i < str.length; i++)
    {
        if(str[i] == ")" && right < left)
        {
            right += 1;
        }
        else if(str[i] == ")" && right >= left)
        {
            return false;
        }
        else if(str[i] == "(" )
        {
            left +=1
        }
    }

    return right == left;
}

console.log(parensValid('()'));
console.log(parensValid('(())'));
console.log(parensValid('(q(a)(x)(!(7(xx)(34)(2, 7, 11))))'));
console.log(parensValid(')('));
console.log(parensValid('(()'));
console.log(parensValid('hello!'));
console.log(parensValid('()())('));

