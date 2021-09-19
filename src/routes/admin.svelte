<div class="text-center">
 <div class="jumbotron text-center" >
     <h1> Admin</h1>
    <div class="card my-3 text-center bg-info" style="width:300px;">

        <form class="my-3 text-center " >
            <input type = "gmail"  class="form-contorl" placeholder="example@gmail.com" id="gmail" >

            <input type=" text"  class="form-contorl" id="username" placeholder="Username" >
            <input type ="password"  class="form-contorl " id="pwd" placeholder="Password" >
            <br>
            <button type="submit"  class="btn  btn-primary" on:click="{admin}">Login</button>
            
        </form>
    {#if auth == "some code "} <Administrator/> {:else } enter something {/if}
    
    </div>
</div>
 </div>
<script  >
    import Administrator from "../components/Administrator.svelte";
   var auth;
   function admin(){
     
   }

</script>