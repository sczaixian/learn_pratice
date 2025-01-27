$("#btn_login").click(function () {
    $.ajax({
        url: '/blog_mgodb/login/',
        type: "post",
        data: {
            'username': $("#username").val(),
            'password': $("#password").val(),
            'remember': $("#remember").is(':checked'),
            'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),
        },
        success: function (data) {
            console.log(data);
            console.log(data.serialize())
            if (data.user) {
                window.location.href = '/blog_mgodb/'
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