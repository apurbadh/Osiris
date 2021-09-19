<script type="module">
    export async function load({params}){
        return {
            props: {
                pagename: params.id
            }
        }
    }
</script>

<script>
    let pagename;
let messages = []
setTimeout(() => {
    fetch("localhost:8000/api/chat/" + pagename).then(res =>res.json()).then(res => messages = res)
}, 2000)
</script>


<ul>
{#each messages as message}
    <li>{message}</li>
{/each}
</ul>