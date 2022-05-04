/* 
  Missing Value
  You are given an array of length N that contains, in no particular order,
  integers from 0 to N . One integer value is missing.
  Quickly determine and return the missing value.
*/

const nums1 = [3, 0, 1];
const expected1 = 2;

const nums2 = [3, 0, 1, 2];
const expected2 = null;
// Explanation: nothing is missing

/* 
Bonus: now the lowest value can now be any integer (including negatives),
instead of always being 0. 
*/

const nums3 = [2, -4, 0, -3, -2, 1];
const expected3 = -1;

const nums4 = [5, 2, 7, 8, 4, 9, 3];
const expected4 = 6;

// nums1.sort()
// nums2.sort()
nums3.sort()
// nums4.sort()

// console.log(nums1)
// console.log(nums2)
console.log(nums3)
// console.log(nums4)

/**
 * Determines what the missing int is in the given unordered array of ints
 *    which spans from 0 to N where only one int is missing. With this missing
 *    int, a consecutive sequence of ints could be formed from the array.
 * Bonus: Given ints can span from N to M (start and end anywhere).
 * @param {Array<number>} unorderedNums
 * @returns {number|null} The missing integer needed to be able to form an unbroken
 *    consecutive set of integers from the given array or null if none is missing.
 */
function missingValue(unorderedNums)
{
    unorderedNums.sort()
    console.log(unorderedNums)
    let lowestNum = unorderedNums[0];
    for(let i =1; i<unorderedNums.length; i++)
    {
        if(unorderedNums[i] < lowestNum) 
        {
            lowestNum = unorderedNums[i];
        }
    }
    console.log(lowestNum)
    for(var i = 0; i < unorderedNums.length;i++)
    {
        
        if(unorderedNums[i] != i)
        {
            return i;
        }
    }
    return null
}

function missingValue(unorderedNums) {
    let hashMap = {}
    let min = Number.POSITIVE_INFINITY;
    for(let i of unorderedNums){
        if (i < min){
            min = i;
        }
        hashMap[i] = null;
    }
    for(let i in hashMap){
        if(min in hashMap){
            min += 1;
        }
        else{
            return min;
        }
    }
    return null;
}




console.log(missingValue(nums3))
console.log(missingValue(nums4))







/* 
Array: Mode

Create a function that, given an array of ints,
returns the int that occurs most frequently
What if there are multiple items that occur the same number of time?
    - return all of them (in an array)
    - what if all items occur the same number of times?
- return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];
//  - order doesn't matter

/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 */
function mode(nums) {
    if(nums.length == 0 || nums.length == 1)
    {
        return nums
    }
            // define new empty object
    let newObj = {} ;
        // for loop to iterate through passed array
    for(let i=0; i<nums.length; i++) {
        // if the index value of the array does not exist as a key in our object, create a new key and set value to 1
            if (!newObj.hasOwnProperty(nums[i])) {
                newObj[nums[i]] = 1;
            }
            // if the index value of the array does exist, add 1 
            else {
                newObj[nums[i]]++;
            }
        }
        //for loop t iterate through the keys of previously made object
      for(key in newObj){
        
        if(newObj[key] == '1'){
          //return key value
          newObj.pop[key];
        }
      }
      //if no key values were found only once, return null
      return null;
    }

    console.log(mode(nums1))
    console.log(mode(nums2))
    console.log(mode(nums3))
    console.log(mode(nums4))
    console.log(mode(nums5))

    function mode(nums) {
        if(nums.length == 0){
            return [];
        }
        if(nums.length == 1){
            return nums;
        }
    
        let hashMap = {};
        for(let i = 0; i < nums.length; i++){
            if(hashMap[nums[i]] != undefined){
                hashMap[nums[i]] += 1;
            }
            else{
                hashMap[nums[i]] = 1;
            }
        }
        let max = Number.NEGATIVE_INFINITY;
        let result = [];
        let allSame = true;
        for (let key in hashMap){
            key = parseInt(key, 10)
            if(hashMap[key] > max){
                max = hashMap[key]
                result = [key]
            }
            else if(hashMap[key] == max){
                result.push(key)
            }
            else{
                allSame = false;
            }
        }
        if(allSame == true){
            return [];
        }
        else{
            return result;
        }
    }