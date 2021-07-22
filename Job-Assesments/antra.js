// How to reverse a string 

// function reverseString(string){
//   if(typeof string !== "string"){
//     return "Not a String"
//   } else {
//     return string.split('').reverse().join('');
//   }
// }

// reverseString("abcd e");
// reverseString("233c de");

// create a function take a string as input and remove the duplicate.

// function removeDuplicateCharacters(string) {
//   return string
//     .split('')
//     .filter(function(item, index, self) {
//       return self.indexOf(item) == index;
//     })
//     .join('');
// }

// removeDuplicateCharacters("remember");

// create a function take a string as input and return a double string.

// function double(input){
//   return input.repeat(2);
// }
// double("hello");

// create a function that takes a string as input and returns each letter in the word doubled string.

// function doubleLetters(string){
//   let stringDouble = "";

//   for(let index=0; index<string.length; index++){
//     stringDouble += string[index]+string[index];  
//   }
//   return stringDouble
// }

// doubleLetters('abc');


//create a function take a string statement as input and return a reverse word of the statement

// function foo(sentence){
//   let word = sentence.split(" ");
//   let reversedPhrase = word.reverse();
//   return reversedPhrase.join(" ");
// }

// foo("abc bcd");

// create a function take a string as input and replace 'a' to '*'


