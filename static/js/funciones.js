/*$(document).ready(function(){
	var altura = $('.navbar-fixed-top').offset().top;
	$(window).on('scroll', function(){
		if ( $(window).scrollTop() > altura ){
			$('.navbar-fixed-top').addClass('navbar-sticky');
		} else {
			$('.navbar-fixed-top').removeClass('navbar-sticky');
		}
	});
});*/
/*
$(document).ready(function(){
	var altura = $('.navbar-fixed-top').offset().top;
	$(window).on('scroll', function(){
		if ( $(window).scrollTop() > altura ){
			document.'navbar-fixed-top.style.backgroundColor'.setAttribute = 'transparent';
		} else {
			document.'navbar-fixed-top.style.backgroundColor' = '#81BEF7';
		}
	});
});*/
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
});
$(document).ready(function(){
	$(".collapse").on('show.bs.collapse', function(){
		$(".escudoRight").hide();
	});
});
$(document).ready(function(){
	$(".collapse").on('hide.bs.collapse', function(){
		$(".escudoRight").show();
	});
});
$(document).ready(function(){
	var hgroupS = $(".video").width();
	alert("el video cambio");
	$(".video").resize(function(){
		$(".hgroup").width(hgroupS+"rem"); 

}