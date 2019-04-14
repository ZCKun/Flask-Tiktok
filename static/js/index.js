// aos滚动效果
AOS.init({
    duration: 900,
});

// 背景切换
const lightMode = document.querySelector('.sun');
const darkMode = document.querySelector('.moon');

const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;

lightMode.onclick = function () {
    document.documentElement.setAttribute('data-theme', 'dark');
    lightMode.style = "display: none";
    darkMode.style = "display: block";
    localStorage.setItem('theme', 'dark');
};

darkMode.onclick = function () {
    document.documentElement.setAttribute('data-theme', 'light');
    lightMode.style = "display: block";
    darkMode.style = "display: none";
    localStorage.setItem('theme', 'light');

};

if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);

    if (currentTheme === 'dark') {
        lightMode.style = "display: none";
        darkMode.style = "display: block";
    }
}

/**
 * 正常代码
 */
// {#ajax load more#}
    $(function () {
        var $video = $('.video-container');
        var $loading = $('.loading-container');
        // {#var htmlNodes = '';#}
        var isEnd = false;
        var status = 1;

        $(window).scroll(function () {
            if (isEnd)
                return;
            if ($(window).scrollTop() === $(document).height() - $(window).height()) {
                $.ajax({
                    type: "GET",
                    url: "/more",
                    success: function (resp) {
                        if (resp === 0){
                            $video.html("<h1 style='--font-color: #ff0006'>获取视频列表失败!</h1>");
                        }
                        var html = '';
                        var r = JSON.parse(resp);
                        for (var i = 0; i < r.length; i++) {
                            result = r[i];
                            // {#parseInt(Math.random() * (max - min + 1) + min, 10)
                            //     max 最大值 ，min 最小值#}
                            var a_i_aos_dealy = parseInt(Math.random() * (300 - 10 + 1) + 10, 10);
                            var a_i_aos_duration = parseInt(Math.random() * (600 - 400 + 1) + 400, 10);
                            var a_i_aos = parseInt(Math.random() * (3 + 1), 10);

                            var v_d_aos_dealy = parseInt(Math.random() * (300 - 10 + 1) + 10, 10);
                            var v_d_aos_duration = parseInt(Math.random() * (600 - 400 + 1) + 400, 10);
                            var v_d_aos = parseInt(Math.random() * (3 + 1), 10);

                            var signature = "";
                            // {# 个性签名有可能为空 #}
                            if (result['author_infos']['signature'] !== "") {
                                signature = result['author_infos']['signature'];
                            }
                            html += '<div class="v-c">'
                                + '<div class="video-info">'
                                // {#作者信息#}
                                + '<div class="author-info" data-a_i_aos-delay="' + a_i_aos_dealy
                                + '" data-a_i_aos-duration="' + a_i_aos_duration + '" data-a_i_aos="' + a_i_aos + '" data-aos-once="true">'
                                // {#头像#}
                                + '<div class="avatar">'
                                + '<img clas="avatar_thumb" src="' + result["avatar_infos"]["url"][0] + '" alt="">'
                                + '</div>'
                                // {#用户名#}
                                + '<div class="nn-wrap">'
                                + '<span class="nickname">' + result["author_infos"]["nickname"] + '</span>'
                                + '</div>'
                                // {#个性签名#}
                                + '<div class="st-wrap">'
                                + '<span class="signature">' + signature + '</span>'
                                + '</div>'
                                + '</div>'
                                // {#视频简介#}
                                + '<span class="video-desc" data-a_i_aos-delay="' + v_d_aos_dealy
                                + '" data-a_i_aos-duration="' + v_d_aos_duration + '" data-a_i_aos="' + v_d_aos + '">'
                                + result["video_infos"]["description"] + '</span>'
                                + '</div>'
                                // {#视频#}
                                + '<div style="text-align: center">'
                                + '<video id="' + result["aweme_id"] + '" class="video"'
                                + ' src="' + result["video_infos"]["url"][0] + '" onclick="if(this.paused){this.play()}else{this.pause()}"></video>'
                                + '</div></div>\n';
                        }
                        $video.append(html);
                        AOS.refresh();
                    },
                    beforeSend: function () {
                        $loading.show();
                    },
                    complete: function () {
                        // {#$(window).scrollTop(0);#}
                        $loading.hide();
                    }
                });
            }
        });
    });
