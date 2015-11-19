function toggle_images() {
     var imgs = document.querySelectorAll("img");
     for(var i = 0; i < imgs.length; i++) {
	       if (imgs[i].style.display == "none") {
  	            imgs[i].style.display = "block";
   	       } else {
   	            imgs[i].style.display = "none";
   	       }
   	   }
}		    

