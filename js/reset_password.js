async function reset_password() {
    console.log("reset_password")

    const form = event.target;
    console.log(form);
    const conn = await fetch("/api-create-new-password", {
     method: "POST",
     body: new FormData(form),
    });

    window.location.href="/"


    // const data = await conn.json()
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
    // console.log(data)

    // if (connection.ok) {
    //     location.href = "/"
    // } else {
    //         const errorMessage = data.info;
    //         console.log(errorMessage)
    
    //         document.querySelector("#errorModal").classList.remove("hidden");
    //         document.querySelector("#errorMessage").textContent = errorMessage
    // }
};
   