$(document).ready(function() {
	$(window).on('load', function () {
		$('.preloader').fadeOut().end().delay(400).fadeOut('slow');
		$('body, html').animate({scrollTop: 0}, 200);
	});

	$(window).on("scroll", function() {
		if ($(window).scrollTop() > 90) {
			$(".header .navbar").css("background-color", "#151515");
			$("#btn-go-top").css("display", "block");
		}
		else {
			if ($(window).width() > 991)
				$(".header .navbar").css("background-color", "transparent");
			$("#btn-go-top").css("display", "none");
		}
	});

	$("#btn-go-top").on('click', function() {
		$('body, html').animate({scrollTop: 0}, 300);
		return false;
	});
});