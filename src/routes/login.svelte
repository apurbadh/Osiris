<div class="ocean">
  <div class="wave"></div>
  <div class="wave"></div>
  <div class="wave"></div>
</div>
<div class="login-page">
    


    <div class="form text-center">
      <div class="icon" style=" margin-bottom: 25px;">
        <img src="/osiris.png" alt="oka" height="100px%" width="100px">
      </div>  
      
      <form class="register-form">
        <input type="text" placeholder="Username"/>
        <input type="password" placeholder="Password"/>
        <input type="text" placeholder="email address"/>
        <button>create</button>
        <p class="message">Already registered? <a href="/">Sign In</a></p>
      </form>
      <form class="login-form">
        <input type="text" placeholder="Username"/>
        <input type="password" placeholder="Password"/>
        <button>login</button>
        <p class="message">Not registered? <a href="/register">Create an account</a></p>
      </form>
    </div>
  </div>
  <div class="header">
  
</div>
<div class="canvas-wrap">
  <canvas id="canvas"></canvas>
</div>
<div class="content">
  
</div>



<style>
  .login-page {
    width: 360px;
    padding: 8% 0 0;
    margin: auto;
  }
  .form {
    position: relative;
    z-index: 1;
    background: #FFFFFF;
    max-width: 360px;
    margin: 0 auto 100px;
    padding: 45px;
    text-align: center;
    box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
  }
  .form input {
    font-family: "Roboto", sans-serif;
    outline: 0;
    background: #f2f2f2;
    width: 100%;
    border: 0;
    margin: 0 0 15px;
    padding: 15px;
    box-sizing: border-box;
    font-size: 14px;
  }
  .form button {
    font-family: "Roboto", sans-serif;
    text-transform: uppercase;
    outline: 0;
    background: #4CAF50;
    width: 100%;
    border: 0;
    padding: 15px;
    color: #FFFFFF;
    font-size: 14px;
    -webkit-transition: all 0.3 ease;
    transition: all 0.3 ease;
    cursor: pointer;
  }
  .form button:hover,.form button:active,.form button:focus {
    background: #43A047;
  }
  .form .message {
    margin: 15px 0 0;
    color: #b3b3b3;
    font-size: 12px;
  }
  .form .message a {
    color: #03c04a;
    text-decoration: none;
  }
  .form .register-form {
    display: none;
  }


</style>
  <svelte:head>
    <title>Login</title>
    <meta name="robots" content="noindex nofollow" />
    <html lang="en" />
  </svelte:head>