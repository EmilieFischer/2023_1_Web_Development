async function follow(){
    const frm = event.target
    const conn = await fetch("/api-follow", {
        method: "POST", 
        body: new FormData(frm)
    })
    const data = await conn.json()
    console.log(data)

    const unfollow_user = frm.parentNode.insertAdjacentHTML("beforeend", 
        `<form id="${data.follower_id}" onsubmit="unfollow_user(); return false" method="POST" class="grid">
        <input style="display:none" name="user_followee_id" type="text" value="${data.followee_id}">
        <button type="submit" class="stroke-gray-500 rounded-full inline-block border border-gray-500 py-2 hover:bg-zinc-900 px-4 text-base">
        Following
        </button>
        </form>`
    ) 
    frm.remove()
    }

    async function unfollow_user(){
        const frm = event.target
        const conn = await fetch("/api-unfollow", { 
            method: "POST", 
            body: new FormData(frm) 
    })

    const data = await conn.json()
    console.log(data)

    const follow_user = frm.parentNode.insertAdjacentHTML("beforeend",
        `<form id="${data.follower_id}" onsubmit="follow(); return false" method="POST" class="grid">
        <input style="display:none" name="user_followee_id" type="text" value="${data.followee_id}">
        <button type="submit" class="stroke-gray-500 rounded-full inline-block border border-gray-500 py-2 hover:bg-zinc-900 px-4 text-base">
        Follow
        </button>
        </form>`
    )
    frm.remove()
}