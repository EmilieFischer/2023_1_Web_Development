// async = run multible functions in the browser at the same time
async function login(){
    console.log("login")
    // the event is = onsubmit, the target is = the form cause it triggeres the onsubmit. The code will know which form automatically 
    const frm = event.target
    console.log(frm)
    // creates the connection, "the tunnel", and then wait for the tunnel to be made.
    const conn = await fetch("/api-login", {
        method: "POST", 
        // building the form: i want to post whatever i have in the form
        body: new FormData(frm)
    })
    // // what we will get back from the server after the tunnel is build. We want to get some text back from the server
    const data = await conn.json()
    const info = data.info
    const cause = data.cause
    console.log(data)
    if(info === "Login failed"){
        console.log("Her kan vi gøre noget")
        console.log(cause)
    } else{
        console.log("Succes")
    }
    // // data = the text that I get back in the response from the server

}