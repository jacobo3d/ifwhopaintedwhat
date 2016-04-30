onload = function(){
	var button = document.querySelector("button");
	var logResponse = function () {
		console.log(this.responseText);
	}
	button.onclick = function() {
		var post_parameters = "./stylize"
		var req = new XMLHttpRequest()
		req.addEventListener("load", show_output)
		req.open("post", post_parameters, true)
		req.send()
	}
}
