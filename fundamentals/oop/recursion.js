/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;

// /
//  * Recursively sum the given int and every previous positive int.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {number} num
//  * @returns {number}
//  /
function recursiveSigma(num) {
    num = Math.floor(num);
    
    if(num == 0)
    {
        return 0;
    }
    else
    {
        return num + recursiveSigma(num - 1);
    }

}
console.log(recursiveSigma(num1));
console.log(recursiveSigma(num2));



/**/

/* 
  Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

const nums2 = [1];
const expected2 = 1;

const nums3 = [];
const expected3 = 0;

// /
//  * Add params if needed for recursion
//  * Recursively sums the given array.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<number>} nums
//  * @returns {number} The sum of the given nums.
//  /

function sumArr(nums, counter) {

if(counter == 0)
{
    return nums[0];
}
else
{
    
    return sumArr(nums + sumArr[counter - 1])
    
}

}


console.log(sumArr(nums1, counter = nums1.length));
console.log(sumArr(nums2, counter = nums2.length));
console.log(sumArr(nums3, counter = nums3.length));

/**/