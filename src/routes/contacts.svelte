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