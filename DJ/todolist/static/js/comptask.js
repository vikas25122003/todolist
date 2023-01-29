colors = {
    "HOME": "green",
    "WORK": "blue",
    "PERSONAL": "orange",
    "MEETING": "red",
    "EXERCISE": "#f0740e",
    "APPOINTMENTS": "hotpink",
    "BILLS": "brown",
    "BIRTHDAY": "gold",
    "ACCOUNTS": "magenta",
    "CLASS": "teal",
    "MOVIE": "#8a8480",
    "OTHER": "black",
}

let cat = document.querySelectorAll(".category-color")
let title = document.querySelectorAll(".title")
let maintaskdiv = document.querySelectorAll(".main-task-div")

cat.forEach((task) => {
    task.style.background = colors[task.id]
})
title.forEach((task) => {
    task.style.color = colors[task.id]
})