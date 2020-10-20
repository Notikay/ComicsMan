$(document).ready(function() {
	$(window).on("scroll",function() {
		if ($(window).width() < 992)
			$(".navbar").css("background-color", "#151515");
		else {
			if ($(window).scrollTop() > 90)
				$(".navbar").css("background-color", "#151515");
			else
				$(".navbar").css("background-color", "transparent");
		}
	});
});