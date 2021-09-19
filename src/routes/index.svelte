<script>
    import Nav from "../components/Nav.svelte"
    import Search from "../components/Search.svelte"
    import Footer from "../components/Footer.svelte";
</script>



<div class="" >
<div class="jumbotron" style="margin: 0;">
    <Search/>
<div class='box text-center'>
    <div class='wave -one'></div>
    <div class='wave -two'></div>
    <div class='wave -three'></div>
    <div class="text-center" > </div>

    <img src="/osiris-rmbg.png" class=" img-fluid" style=" padding:0px; height:150px" alt="main logo">
    <h2>OSIRIS</h2>

    <div class="wrapper" > 
        <div class=" title typing">
              Live Healthy, Live Better

        </div>
    </div>
    
</div>
            
<div class="text-center">
<Nav/>
<Search/>
</div>
</div>
</div>



<Footer/>

<style>


.wrapper {
height: 100%;
/*This part is important for centering*/
display:flex;
align-items:center;
justify-content: center;
}
@keyframes typing {
from { width: 0}
to {width: 30em;}
}

@keyframes blink {
0% {
border-color: transparent

}
}

.box {
    /* background-color: #d4fce3; */
    /* background-color: #d2e3fc; */
    background-color: #d2fcf5;
    height: 300px;
    border-radius: 100px;
    box-shadow: 0 2px 30px rgba(black, .2);
    background: lighten(#ffff, 10%);
    position: relative;
    overflow: hidden;
    transform: translate3d(0, 0, 0);
    }

.wave {
    opacity: .5;
    position: absolute;
    top: 0%;
    left: 60%;
    background: limegreen;
    width: 500px;
    height: 500px;
    margin-left: -0;
    margin-top: -200px;
    transform-origin: 0% 60%;
    border-radius: 50%;
    animation: drift 4000ms infinite linear;
}

.wave.-three {
    margin-left: -300px;
    margin-top: -300px;
    animation: drift 4300ms infinite linear;
    background-color: lightgreen;
    border-radius: 50%;

}

.wave.-two {
    position:absolute;
    margin-left: 250px;
    animation: drift 4300ms infinite reverse linear;
    opacity: .5;
    border-radius: 50%;
    background: greenyellow;
}


.box:after {
    content: '';
    display: block;
    left: 0;
    top: 0;
    height: 100%;
    background: linear-gradient(to bottom, rgba(#e8a, 1), rgba(#def, 0) 80%, rgba(white, .5));
    z-index: 1;
    transform: translate3d(0, 0, 0);
}

 .title {
    animation: typing 7s steps(70), blink .5s step-end infinite alternate;
    position: relative;
    white-space: nowrap;
    overflow: hidden;
    border-right: 3px solid;
    font-family: monospace;
    font-size: 1em;
    top: -45%;
    width: 100%;
    line-height: 50px;
    transform: translate3d(0, 0, 0);
    color: black;
} 
@keyframes drift {
    from { transform: rotate(0deg); }
    from { transform: rotate(180deg); }
    from { transform: rotate(360deg); }
}
</style>


<svelte:head>
<title>Home</title>
<meta name="robots" content="noindex nofollow" />
<html lang="en" />
</svelte:head>