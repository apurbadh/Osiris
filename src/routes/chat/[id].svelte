<script>

    let pagename = 1;
    let mes;
let messages = []
const sendMessage = () => {
    fetch("http://localhost:8000/api/chat/send?message=" + mes, {
        method: "post"
    }).then(() => {
        console.log("sent")
    })
}
setTimeout(() => {
    fetch("http://localhost:8000/api/chat/" + pagename).then(res =>res.json()).then(res => {messages = res
    console.log(res)})
}, 2000)
</script>
  <input bind:value={mes}>
    <button on:click={sendMessage}>Send</button>

<ul>
  
{#each messages as message}
    <li>{message}</li>
{/each}
</ul>
