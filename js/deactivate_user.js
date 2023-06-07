async function deactivate_user(){
    console.log("deactivate_user")
    const frm = event.target
    const conn = await fetch("/api-deactivate-user", {
        method: "POST", 
        body: new FormData(frm)
    })
}