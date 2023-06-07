async function delete_user(userId){
    var remove_user = document.getElementById('user_' + userId);
    remove_user.remove();

    console.log(event.target.form.id)
    const user_id = event.target.form.id
    const conn = await fetch(`delete-user/${user_id}`, {
        method : "DELETE"
    })
    const data = await conn.text()
    console.log(data)
}