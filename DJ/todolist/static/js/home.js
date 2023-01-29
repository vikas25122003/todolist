var i = 0;
let firstline = 'Welcome To Code List .';

var speed = 120;

function typeWriter(mytext = firstline) {
    if (i < mytext.length) {
        document.querySelector("#firstline").innerHTML += mytext.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}

typeWriter(firstline);

