$("#btn_login").click(function () {
    $.ajax({
        url: '/blog/login/',
        type: "post",
        data: {
            'username': $("#username").val(),
            'password': $("#password").val(),
            'remember': $("#remember").is(':checked'),
            'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),
        },
        success: function (data) {
            console.log(data);
            if (data.user) {
                window.location.href = '/blog/'
            } else {
                if (data.msg) {
                    $('.login_error').text(data.msg).css({'color': 'red', "margin-left": '10px'})
                    setTimeout(function () {
                        $('.login_error').text('')
                    }, 3000)
                }
            }
        },
        error: function (data) {
            console.log(data);
            $('.login_error').text(data.msg).css({'color': 'red', "margin-left": '10px'})
            setTimeout(function () {
                $('.error').text('')
            }, 1000)
        }
    })

})