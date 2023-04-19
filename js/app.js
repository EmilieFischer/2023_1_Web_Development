function hide_signup_modal(){
    document.getElementById("authentication-modal").classList.add("hidden");
    document.getElementById("login-modal").style.display="flex";
}


function hide_login_modal(){
    document.getElementById("login-modal").classList.add("hidden");
    document.getElementById("authentication-modal").style.display="flex";
}
