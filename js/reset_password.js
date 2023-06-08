async function reset_password() {
    console.log("reset_password")

    const form = event.target;
    console.log(form);
    const conn = await fetch("/create-new-password", {
     method: "POST",
     body: new FormData(form),
    });

    window.location.href="/"

}
   