async function forgot_password(){
    console.log("forgot_password")
    
    const frm = event.target
    const conn = await fetch("/send-forgot-password-email", {
        method: "POST", 
        body: new FormData(frm)
    });

    window.location.href="/"


     // what we will get back from the server after the tunnel is build. We want to get some text back from the server
    //  const data = await conn.json()
    //  const {info, cause} = data
 
    //  if(info){
 
    //      if(info === "Reset password succes"){
    //          console.log("Succes")
    //          window.location.href="/"
    //      } else {
    //          console.log(cause)
    //      }
    //  }
 

    // const data = await connection.json();
    // data.info === "password reset" ? location.href = `/`;
    // console.log(data)
    // data.info === "password reset" ? location.href = `/` : displayError();

    // function displayError() {
    //     const errorMessage = data.info;
    //     console.log(errorMessage)

    //     document.querySelector("#errorModal").classList.remove("hidden");
    //     document.querySelector("#errorMessage").textContent = errorMessage
    // }
};