async function deactivate_user(){
    console.log("deactivate_user")
    const frm = event.target
    const conn = await fetch("/api-delete-user", {
        method: "POST", 
        body: new FormData(frm)
    })
    // const data = await conn.json()
    // if (!conn.ok) {
    //     console.log("Cannot delete user");
    //     return;
    // }
    // console.log(data)
}