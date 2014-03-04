var login = function () {
	$('#login').bind("click", function () {
		var email = $("#email").val();
		var password = $("#password").val();
		if (email.length === 0 || password.length === 0) {
			alert("write correct email or password");
			return false;
		}
		$.ajax({
			url: "/login",
			method: "POST",
			data: {'email': email, 'password': password},
			dataType: "json",
			success: function (data, textStatus, jqXHR) {
				if (data.login) {
					$('#loginForm').css("display", "none");
					$('#nav-collapse').append('<ul class="nav navbar-nav navbar-right" id="profile"><li><a href="#">' + data.user_id + '</a></li></ul>');
				}
			},
			error: function (jqXHR, textStatus, errorThrown) {
				console.log(errorThrown);
			}
		});
		return false;
	});
	return false;
};
