const baseURL = 'http://localhost:9009/api/babies'

const getAll = document.querySelector("#getBabies")
const babyContainer = document.querySelector(".babiesContainer")

const getAllBabies = () => {
    console.log("Hello")
    axios.get(`${baseURL}`)
    .then((res) => {
        console.log(res)
        // alert(res.data)
        displayBabies(res.data)
    })
    .catch(err => console.log(err))
}

function displayBabies(arr) {
    babyContainer.innerHTML = ``
    for(let i=0; i<arr.length; i++){
        createBabyCard(arr[i])
    }
}
function test () {
    console.log("onclick confirmed");
  };
function createBabyCard(baby) {
    console.log(baby)
    let action1 = baby.action1.name
    console.log(typeof action1)
    const babyCard = document.createElement('div')
    babyCard.classList.add("babiesCard")
    babyCard.innerHTML += `<img alt="baby picture" src=${baby.imageURL} class="babyPicture"/>
    <p class="babyName">${baby.name}<br>HP=${baby.health}</p>
    <div class="babyButtonContainer">
        <button onclick="showStats('${baby.action1.name}', '${baby.action2.name}', '${baby.action3.name}')">Show Stats</button>
    </div>
    `
    babyContainer.appendChild(babyCard)
}

function showStats(p1,p2,p3){
    console.log(p1, p2, p3)
    document.querySelector(".babiesCard").innerHTML +=
    `<p>Action 1: ${p1}<br> Action 2: ${p2}<br> Action 3: ${p3}</p>`
}
// axios.get

getAll.addEventListener("click", getAllBabies)