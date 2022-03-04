// This is a simple cipher to transfer the value of each character to its
// character code. Then I wanted to see if I could add 1 more layer, a simple
// addition of another number, 42. And then just reverse it to decipher. 

// For each character in the password string, I will access the character code
// using string.charCodeAt(index), and push each character code +42 into a new
// array, then concatenate the array back into a string with each one separated
// by a '|'.
// to Decipher it, the new function will have to make the string into an array
// using str.split("|"). Then iterate through the array and for each index,
// then convert the codes back into the original characters using the 
// String.fromCharCode(array[i]-42)

function cipher(str) {
  let ciphArr = []
  for(let i = 0; i<str.length; i++){
    // let zorp = str.charCodeAt(i)+42
    ciphArr.push(str.charCodeAt(i)+42)
  }
    let squishyCipher = (ciphArr.toString()).replace(/,/g,'|')
    return squishyCipher
}

let crypted = cipher("I love Cryptography!")

console.log(crypted)

function decipher(crypt) {
  let cryptArr = crypt.split('|')
  for(let i=0; i<cryptArr.length; i++){
    cryptArr.splice(i,1,String.fromCharCode(cryptArr[i]-42))
  }
  let cryptStr = cryptArr.toString()
  return cryptStr.replace(/,/g,'')
}

console.log(decipher(crypted))


/*
I chose the 2013 Adobe data breach. 
Thesis: The Adobe data breach of 2013 represents a shifting paradigm in world affairs
vis-a-vis the current output of user input data within the frame of the psychoanalytical
framework, and trickled down through society primarily by means of organic transparency
and dissemination by FBI officials led by Burt Macklin, FBI. 
Anyway, hackers breached Adobe's databases and stole over 3 million users' personal 
credit card information and 150 million usernames and passwords from Adobe's registered
users. 

*/