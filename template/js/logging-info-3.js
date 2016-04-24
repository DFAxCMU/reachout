$(document).ready(function() {
    $("#log-qinfo").click(function(){
        var intertitle = $(".inter-title").attr("data-title")
        var interdescription = $(".inter-description").attr("data-description")
        var q1 = $(".q1").attr("data-q1")
        var q2 = $(".q2").attr("data-q2")
        var q3 = $(".q3").attr("data-q3")
        var q4 = $(".q4").attr("data-q4")
        var q5 = $(".q5").attr("data-q5")
        var q5 = $(".q6").attr("data-q6")
        var data = {
            "ititle": intertitle,
            "idescription": interdescription,
            "q1":q1,
            "q2":q2,
            "q3":q3,
            "q4":q4,
            "q5":q5,
            "q6":q6

        };
        
        $.ajax({
        type: "POST",
        url: "/log_all_info",
        data: data,
        beforeSend: function (xhr) {
          xhr.withCredentials = true;
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function(data) {
            return
        },
        async: true
        });
    });
}