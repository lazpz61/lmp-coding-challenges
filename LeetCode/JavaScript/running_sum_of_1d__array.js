// Given an array nums. We define a running sum of an 
// array as runningSum[i] = sum(nums[0]…nums[i]).

// Return the running sum of nums. 


function runningSum(nums) {
    let result = []
    let currentSum = 0;
  
    for(let i = 0; i < nums.length; i++) {
      let currentValue = nums[i]
  
      currentSum += currentValue;
      result.push(currentSum);
    }
  
    return result;
  }
  
  console.log(runningSum([2,3,4,5]));
