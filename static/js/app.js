onload = function(){
	var button = document.querySelector("button");
	var logResponse = function () {
		button.disabled = false;
		console.log(this.responseText);
	}
	button.onclick = function() {
		button.disabled = true;
		var post_parameters = "./stylize";
		var req = new XMLHttpRequest();
		req.addEventListener("load", logResponse);
		req.open("post", post_parameters, true);
		req.send();
	}
}
