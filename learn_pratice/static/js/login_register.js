$("#btn_login").click(function () {
    $.ajax({
        url: '/blog/login/',
        type: "post",
        data: {
            'username': $("#username").val(),
            'password': $("#password").val(),
            'remember': $("#remember").val(),
            'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),
        },
        success: function (data) {
            console.log(data);
            if (data.username) {
                location.href = '/blog/'

            } else {
                if (data.msg) {
                    // alert(data.msg)
                    alert('else')
                }
                // alert('-----');
                // $('.error').text(data.msg).css({'color': 'red', "margin-left": '10px'})
                // setTimeout(function () {
                //     $('.error').text('')
                // }, 1000)
            }
        },
        error: function (data) {
            console.log(data);
            alert('error')
            // if (data.msg) {
            //     alert(data.msg)
            // }
        }
    })

})