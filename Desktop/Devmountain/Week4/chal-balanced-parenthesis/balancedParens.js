// Sample Strings
let sample1 = "This ( is unbalanced."
let sample2 = "(This (is (a) balanced) string.)"
let sample3 = "This is () also ) unbalanced."
let sample4 = "Balanced."

// // Write your solution below:

// let arr = str.split('')
// arr.filter((elem) => {
//     elem.
// })

function balancedPar(str) {
    let arr = str.split('')
    let arrOpen = []
    let arrClosed = []
    for(i=0; i<arr.length; i++){
        if(arr[i]==='('){
            arrOpen.push(arr[i])
        }else if(arr[i]===')'){
            arrClosed.push(arr[i])
        }
    // }if(arrOpen.length === arrClosed.length){
    //     return true
    // }else {
    //     return false
    }return arrOpen.length === arrClosed.length
}
console.log(balancedPar(sample3))