// async = run multible functions in the browser at the same time
async function signup(){
    console.log("signup")
    // the event is = onsubmit, the target is = the form cause it triggeres the onsubmit. The code will know which form automatically 
    const frm = event.target.form
    console.log(frm)
    // creates the connection, "the tunnel", and then wait for the tunnel to be made.
    const conn = await fetch("/api-sign-up", {
        method: "POST", 
        // building the form: i want to post whatever i have in the form
        body: new FormData(frm)
    })
    // // what we will get back from the server after the tunnel is build. We want to get some text back from the server
    const data = await conn.json()
    if (!conn.ok) {
        console.log("Cannot login");
        return;
    }
    console.log(data)
    // // data = the text that I get back in the response from the server

}