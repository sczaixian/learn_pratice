$("#btn_login").click(function () {
    $.ajax({
        url: '/blog/paginator/',
        type: "post",
        data: {
            'username': $("#username").val(),
        },
        success: function (data) {
            console.log(data);
            if (data.articles) {
                // window.location.href = '/blog/'
            } else {
                if (data.msg) {
                    console.log(data);
                }
            }
        },
        error: function (data) {
            console.log(data);
        }
    })

})