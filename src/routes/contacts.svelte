<<<<<<< HEAD
<script type="text/javascript">
	function getData(){
		let token = document.cookie.substring(document.cookie.indexOf("token="), document.cookie.length)
		token = token.substring(0, token.indexOf(";") == -1 ? token.length : token.indexOf(";"))
		token = token.replace("token=", '')
		fetch("http://localhost:8000/api/doctor/1", {
			headers : {
				Authorization: `Bearer ${token}`
			}
		}).then(res => res.json()).then(res => console.log(res))
	}
</script>

<div><button on:click={getData}>Free POrn</button>
</div>
=======
<div class="row">
    <div class="card my-3 col card-info" style="width:300px;">
        <div class="card-header">Header</div>
        <div class="card-body">Content</div>
        <div class="card-footer">Footer</div>
    </div>
    <div class="card my-3 col card-info" style="width:300px;">
        <div class="card-header">Header</div>
        <div class="card-body">Content</div>
        <div class="card-footer">Footer</div>
    </div>
    <div class="card my-3 col card-info" style="width:300px;">
        <div class="card-header">Header</div>
        <div class="card-body">Content</div>
        <div class="card-footer">Footer</div>
    </div>
</div>

<svelte:head>
<title>Avaible Doctors</title>
<meta name="robots" content="noindex nofollow" />
<html lang="en" />
</svelte:head>
>>>>>>> refs/remotes/origin/frontend
