let options = document.querySelectorAll(".option-div");
console.log(options)
let mycolors = ['#e3b212', '#1ad64c', '#c61ad6', '#e31224',]


options.forEach((option, count) => {
    console.log(count)
    option.style.background = mycolors[count];
})