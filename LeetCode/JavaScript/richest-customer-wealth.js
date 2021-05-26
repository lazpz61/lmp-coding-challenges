/*
You are given an m x n integer grid accounts where accounts[i][j] is 
the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth

*/


const maximumWealth = function(accounts) {
    let ans = 0;
    for(let i =0;i<accounts.length;i++){
        let res = 0;
        for(let j = 0;j<accounts[i].length;j++){
            res+=accounts[i][j];
        }
       ans = Math.max(ans,res);
    }
    return ans;
};

maximumWealth([[2,3,4],[5,6,10]]);


