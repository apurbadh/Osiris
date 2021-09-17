
<body class=" bg-dark" >
    <div class="login-page">
    
        <div class="form text-center">
          <div class="icon" style=" margin-bottom: 25px;">
            <img src="/osiris.png" alt="oka" height="100px%" width="100px">
          </div>  
          
          <form >
            <input type="text" id="Name" placeholder="Full name"/>
            <input type="text" id="username" placeholder="Username"/>
            <input type="text" id="email" placeholder="Email address"/>
            <input type="password" id="password" placeholder="Password"/>
            <input type="password" id="confirm_password" placeholder="Confirm Password"/>

            <button>create</button>
            <p class="message">Already registered? <a href="/login">Sign In</a></p>
          </form>
        </div>
      </div>
    </body>
    
    
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

      </style>