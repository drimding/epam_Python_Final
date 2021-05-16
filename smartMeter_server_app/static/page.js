  $(function() {
    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

});

    function submitForm(formId, url) {
        var formdata = $("#".concat(formId)).serializeArray();
        var json_data = {};
        $(formdata ).each(function(index, obj){
            if (obj.name === 'username'){
                json_data.username=obj.value
            }
            if (obj.name === 'email'){
                json_data.email=obj.value
            }
            if (obj.name === 'password'){
                json_data.password=obj.value
            }
        });
        json_data =JSON.stringify(json_data)
        $.ajax({
            type: "POST",
            url: url,
            data: json_data,
            success: function (data) {
                if (data.redirect_url) {
                    XMLHttpRequest.setRequestHeader('Authorization', data.authorization)
                    window.location.href = data.redirect_url;
                }else {
                    data = JSON.stringify(data)
                    alert(data)
                }
            },error: function (data){
                alert(data.statusText + " " + data.status + " " + data.responseJSON.message)
            },
            dataType: "json",
            contentType: "application/json"
        })
    }