let head = document.querySelector('#base_nav');
let body = document.querySelector('body');
body.style.overflowX = 'hidden';

setTimeout(()=>{
    (()=>{
        head.classList.add('nav_display');
    })();
},2000);

let bg_img = document.querySelector("#bg_img");
let hide = document.querySelector("#hide");
console.log(hide)

hide.classList.add("view_img");

setTimeout(()=>{
    hide.style.display = 'none';

},5000);

