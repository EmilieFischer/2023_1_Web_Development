function hide_signup_modal(){
    document.getElementById("authentication-modal").style.display="none";
}

function open_signup_modal(){
    document.getElementById("authentication-modal").style.display="flex";
}

function hide_login_modal(){
    document.getElementById("login-modal").style.display="none";
}

function open_login_modal(){
    document.getElementById("login-modal").style.display="flex";
}

function toggle_signup(){
    document.getElementById("login-modal").style.display="none";
    document.getElementById("authentication-modal").style.display="flex";
}

function toggle_login(){
    document.getElementById("authentication-modal").style.display="none";
    document.getElementById("login-modal").style.display="flex";
}