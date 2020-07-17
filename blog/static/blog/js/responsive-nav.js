var search = document.getElementById("search-div");
var navbar =   document.getElementById("nav-bar");
function displaysearch() {
	
	// var nav-bar =   document.getElementById("nav-bar");
	if (search.className === "search-div") {
		search.className += "responsive";
	} else {
		search.className = "search-div";
		navbar.className = "nav-bar";
	}

}

function displaynav() {
	//var search = document.getElementById("search");
	
	if (navbar.className === "nav-bar") {
		navbar.className += "responsive";
	} else {
		search.className = "search-div";
		navbar.className = "nav-bar";
	}

}
