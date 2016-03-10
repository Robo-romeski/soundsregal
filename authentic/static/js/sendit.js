$(document).ready(function() {

    $('#login').click(function() {

        $.ajax({
            type: "POST",
            url: '/login/',
            data: {
                username: $("#email").val(),
                password: $("#password").val()
            },
            success: function(data)
            {
                if (data === 'Correct') {
                    window.location.replace('/authentic/login');
                }
                else {
                    alert(data);
                }
            }
        });

    });

});