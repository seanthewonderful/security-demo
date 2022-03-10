const toyCar = {
    name: "toy car",
    size: "medium",
    clatters: "a bit",
    weight: "medium"
}
const puzzle = {
    name: "puzzle",
    size: "small",
    clatters: "yes",
    weight: "light"
}
const chair = {
    name: "computer chair",
    size: "large",
    clatters: "no",
    weight: "heavy"
}
const moracca = {
    name: "moracca",
    size: "small",
    clatters: "yes",
    weight: "light"
}

let wishlistt = [toyCar, puzzle, chair, moracca]

// var wishlistt = [
//     {name: "Mini Puzzle", size: "small", clatters: "yes", weight: "light"},
//     {name: "Toy Car", size: "medium", clatters: "a bit", weight: "medium"},
//     {name: "Card Game", size: "small", clatters: "no", weight: "light"}
// ];

var presentss = [
    {size: "medium", clatters: "a bit", weight: "medium"},
    {size: "small", clatters: "yes", weight: "light"}
];

function guessGifts(wishlist, presents) {
    let possiblePresents = []
    for(let i=0; i<wishlist.length; i++){
        for(let j=0; j<presents.length; j++){
            if(wishlist[i].size === presents[j].size && 
                wishlist[i].clatters === presents[j].clatters && 
                wishlist[i].weight === presents[j].weight){
                possiblePresents.push(`Present #${j+1} could be ${wishlist[i].name}.`)
            }
        }
    }return possiblePresents
}

console.log(guessGifts(wishlistt, presentss))
