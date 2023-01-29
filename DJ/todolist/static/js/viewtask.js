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

//-------------------------------------------------------------------
let currentdate = new Date()

let hours = currentdate.getHours()
let minutes = currentdate.getMinutes()
let date = currentdate.getDate()
let month = String(currentdate.getMonth() + 1)
let year = currentdate.getFullYear()

console.log(date, month, year)

let monlen = month.length



if (monlen === 1) {
    var wholecurrentdate = new Date(year + '-0' + month + '-' + date)
    wholecurrentdate = wholecurrentdate.getTime()
} else {
    var wholecurrentdate = new Date(year + '-' + month + '-' + date)
    wholecurrentdate = wholecurrentdate.getTime()
}


console.log(wholecurrentdate)

let dateandtime = document.querySelectorAll(".dateandtime")
let tasktitle = document.querySelectorAll(".title")

console.log(hours)
console.log(minutes)

dateandtime.forEach((date, times) => {

    let duedate = date.querySelector('#duedate')
    let duetime = date.querySelector('#duetime')


    var taskduedate = (duedate.innerHTML) //datelist
    var taskduetime = (duetime.innerHTML) //timelist

    mytaskdate = new Date(taskduedate).getTime()

    taskduetime = taskduetime.split(':')
    taskhour = parseInt(taskduetime[0])
    taskmin = parseInt(taskduetime[1])


    console.log('=======================================')
    console.log(wholecurrentdate)
    console.log(mytaskdate)
    console.log(taskduetime)
    console.log(taskhour)
    console.log(taskmin)
    console.log('=======================================')
    //looping for date calculation

    if (mytaskdate < wholecurrentdate) {
        maintaskdiv[times].style.display = "none";
    } else if (mytaskdate === wholecurrentdate) {
        console.log("samedate")
        if (taskhour > hours) {
            console.log("hour available")
            console.log("alert")
            duetime.classList.add('alert');
        } else if (taskhour === hours) {
            console.log('check minutes')
            if (taskmin > minutes) {
                console.log("hour available")
                console.log("alert")
                duetime.classList.add('alert');
            } else {
                maintaskdiv[times].style.display = "none";
            }
        }
        else {
            maintaskdiv[times].style.display = "none";

        }

    } else {
        console.log("Task Time Available")
    }
})
