async function forgot_password(){
    console.log("forgot_password")
    
    const frm = event.target
    const conn = await fetch("/send-forgot-password-email", {
        method: "POST", 
        body: new FormData(frm)
    });

    window.location.href="/"

}