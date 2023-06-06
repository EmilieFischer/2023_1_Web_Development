async function delete_tweet(tweetId){
    var remove_tweet = document.getElementById('tweet_' + tweetId);
    remove_tweet.remove();

    console.log(event.target.form.id)
    const tweet_id = event.target.form.id
    const conn = await fetch(`delete-tweet/${tweet_id}`, {
        method : "DELETE"
    })
    const data = await conn.text()
    console.log(data)
}