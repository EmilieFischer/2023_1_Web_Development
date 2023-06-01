


// async = run multible functions in the browser at the same time
async function tweet(){
    // the event is = onsubmit, the target is = the form cause it triggeres the onsubmit. The code will know which form automatically 
    const frm = event.target;
    console.log(frm)
    // creates the connection, "the tunnel", and then wait for the tunnel to be made.
    const conn = await fetch("/tweet", {
        method: "POST", 
        // building the form: i want to post whatever i have in the form
        body: new FormData(frm)
    })
    // what we will get back from the server after the tunnel is build
    const data = await conn.json()
    console.log(data)
    // data = the text that I get back in the response from the server
    // point to the form. I want to get the value out of it
    const message = frm.querySelector("input[name ='message']").value
    // const image = frm.querySelector("#image")
    const modal = document.querySelector("#tweet_modal")
    //  modal.style.display='none' = fjerner tweet-modalen når der trykkes på tweet-knappen
    modal.style.display='none' 
    // selects tweets. Before the tweet-element (the section) I want to put some HTML (insertAdjacentHTML('afterbegin')) - vi bruger et så det er det nyeste tweet, der kommer først
    document.querySelector("#tweets").insertAdjacentHTML("afterbegin", 
    `<div class="flex p-2">
<img src="/images/${data.user.user_avatar}" class="h-16 rounded-full">
<!-- right side tweet -->
<!-- user -->
<div class="p-4">
<span class="font-bold flex gap-2 items-center">
${data.user.user_first_name}
${data.user.user_last_name}
<svg
  width="18"
  height="18"
  viewBox="0 0 24 24"
  class="text-sky-500 w-4 h-4 stroke-transparent"
>
  <path
    fill="currentColor"
    d="m8.6 22.5l-1.9-3.2l-3.6-.8l.35-3.7L1 12l2.45-2.8l-.35-3.7l3.6-.8l1.9-3.2L12 2.95l3.4-1.45l1.9 3.2l3.6.8l-.35 3.7L23 12l-2.45 2.8l.35 3.7l-3.6.8l-1.9 3.2l-3.4-1.45Zm2.35-6.95L16.6 9.9l-1.4-1.45l-4.25 4.25l-2.15-2.1L7.4 12Z"
  />
</svg>
  <span class="text-gray-500 font-light text-sm">
    <span class=""> <strong>@</strong>${data.user.user_name} · </span>
  ${data.tweet.tweet_created_at}
  </span>
  <svg
  xmlns="http://www.w3.org/2000/svg"
  fill="none"
  viewBox="0 0 24 24"
  stroke-width="1.5"
  stroke="currentColor"
  class="w-6 h-6 stroke-gray-500 hover:stroke-sky-400 ml-auto"
>
  <path
    stroke-linecap="round"
    stroke-linejoin="round"
    d="M6.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM12.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM18.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0z"
  />
</svg>
</span>
   <!-- tweet text -->
<div class="text-base py-2">${message}</div>
${data.tweet.tweet_image ? `<img src="./images/${data.tweet.tweet_image}"class="w-full mt-4 max-h-96 rounded-lg object-contain"/>`: "" }
  
 
      <!-- icons -->
<div class="flex justify-between mt-4 text-gray-700 mr-24">
  <div class="flex items-center group cursor-pointer">
    <span class="p-2 group-hover:bg-zinc-900 rounded-full">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-4 h-4 stroke-gray-500 group-hover:stroke-sky-600 transition ease-in-out"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"
        />
      </svg>
    </span>
    <span
      class="text-sm text-gray-500 group-hover:text-sky-600 transition ease-in-out ml-2"
      >
      ${data.tweet.tweet_total_messages}

      </span
    >
  </div>
  <div class="flex items-center group cursor-pointer">
    <span class="p-2 group-hover:bg-zinc-900 rounded-full">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-4 h-4 stroke-gray-500 group-hover:stroke-green-600 transition ease-in-out"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99"
        />
      </svg>
    </span>
    <span
      class="text-sm text-gray-500 group-hover:text-green-600 transition ease-in-out ml-2"
      >
      ${data.tweet.tweet_total_retweets}

      </span
    >
  </div>
  <div class="flex items-center group cursor-pointer">
    <span class="p-2 group-hover:bg-zinc-900 rounded-full">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-4 h-4 stroke-gray-500 group-hover:stroke-red-600 transition ease-in-out"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
        />
      </svg>
    </span>
    <span
      class="text-sm text-gray-500 group-hover:text-red-600 transition ease-in-out ml-2"
      ${data.tweet.tweet_total_likes}
      </span
    >
  </div>
  <div class="flex items-center group cursor-pointer">
    <span class="p-2 group-hover:bg-zinc-900 rounded-full">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-4 h-4 stroke-gray-500 group-hover:stroke-sky-600 transition ease-in-out"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z"
        />
      </svg>
    </span>
    <span
      class="text-sm text-gray-500 group-hover:text-sky-600 transition ease-in-out ml-2"
      >
      ${data.tweet.tweet_total_dislikes}
      </span
    >
  </div>
  <div class="flex items-center group cursor-pointer">
    <span class="p-2 group-hover:bg-zinc-900 rounded-full">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-4 h-4 stroke-gray-500 group-hover:stroke-sky-600 transition ease-in-out"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5"
        />
      </svg>
    </span>
  </div>
</div>
</div>
</div>`)

frm.querySelector("#preview").src=""
  }

function handle_preview() {
  document.querySelector('#preview').src=URL.createObjectURL(event.target.files[0]);
}

