
$(document).ready(function(){
	var altura = $('.navbar-fixed-top').offset().top;
	var escudoLeftW = $(".escudoLeft").width();
	var escudoRightW = $(".escudoLeft").width();

	$(window).on('scroll', function(){
		if ( $(window).scrollTop() > altura ){
			$('.navbar-fixed-top').removeClass('navbar-default');
			$('.navbar-fixed-top').addClass('navbar-sticky');
			$(".escudoLeft").width("50px");
			$(".escudoRight").width("50px");
		} else {
			$('.navbar-fixed-top').removeClass('navbar-sticky');
			$('.navbar-fixed-top').addClass('navbar-default');
			$(".escudoLeft").width(escudoLeftW+"px");
			$(".escudoRight").width(escudoLeftW+"px");
		}
	});
	$(".collapse").on('show.bs.collapse', function(){
		$(".escudoRight").hide();
	});
	$(".collapse").on('hide.bs.collapse', function(){
		$(".escudoRight").show();
	});

	$(window).resize(

		function () {    
    		var width = document.documentElement.clientWidth;
    
   			 if (width < 1500 && width >= 900){
     			 document.getElementById('textoVideo').style.fontSize = '10rem';
     			 document.getElementById('lema').style.fontSize = '4rem';
      
   			 }else if (width < 900 && width >= 720){
     			 document.getElementById('textoVideo').style.fontSize = '8rem';
     			 document.getElementById('lema').style.fontSize = '3rem';
      			  $('.btn').addClass('btn-lg');
		    }else if(width < 720 && width >= 580){
     				document.getElementById('textoVideo').style.fontSize = '6rem';
      				document.getElementById('lema').style.fontSize = '2rem';
      				$('.btn.btn-lg').removeClass('btn-lg');
      				$('.btn').removeClass('btn-sm');
	  
    		}
    		else if(width < 580 && width >= 440){
     				 document.getElementById("textoVideo").style.fontSize = "4rem";
      				 document.getElementById('lema').style.fontSize = '1.5rem';
      				 $('.btn.btn-xs').removeClass('btn-xs');
       				$('.btn').addClass('btn-sm');
    		}
    		else if(width<440 && width>=0){
    				document.getElementById("textoVideo").style.fontSize = "3rem";
      				 document.getElementById('lema').style.fontSize = '1rem';
    			  $('.btn.btn-sm').removeClass('btn-sm');
     			 $('.btn').addClass('btn-xs');
   			 }
   			 else{
     			 document.getElementById("textoVideo").style.fontSize = "10rem";
     		  document.getElementById('lema').style.fontSize = '4rem';


    }
}).resize();

});

