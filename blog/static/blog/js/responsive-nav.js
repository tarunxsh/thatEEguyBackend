var search = document.getElementById("search-div");
var navbar =   document.getElementById("nav-bar");
function displaysearch() {
	
	// var nav-bar =   document.getElementById("nav-bar");
	if (search.className === "search-div") {
		search.className += " clicked";
	} else {
		search.className = "search-div";
		navbar.className = "nav-bar";
	}

}

function displaynav() {
	if (navbar.className === "nav-bar") {
		navbar.className += " clicked";
	} else {
		// search div not a feature now
		// search.className = "search-div";
		navbar.className = "nav-bar";
	}

}
