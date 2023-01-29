let options = document.querySelectorAll(".option")
let selectedCategory = document.getElementById("hiddencategory")
console.log(options)

options.forEach((eachoption) => {
    eachoption.addEventListener("click", () => {
        options.forEach((delmarker) => {
            delmarker.classList.remove("selected-option")
        })
        eachoption.classList.toggle("selected-option")
        selectedCategory.value = eachoption.innerHTML
        console.log(selectedCategory.value)
    })
})



var rangevalue = document.getElementById("rangeinput");
let selectvalue = document.getElementById("selected")
rangevalue.onchange = () => {
    selectvalue.innerHTML = rangevalue.value
}
