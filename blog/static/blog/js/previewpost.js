function preview(){
	var postinput = document.getElementById('id_descp');
	var preview_container = document.getElementById('preview-container');
	if(postinput.hidden == false){
		postinput.hidden = true;
		preview_container.innerHTML = marked(postinput.value);
	}
	else {
		postinput.hidden=false;
		preview_container.innerHTML = "";
	}
}