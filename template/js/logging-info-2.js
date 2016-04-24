$(document).ready(function() {
    $("#log-qinfo").click(function(){
        var intertitle = $(".inter-title").attr("data-title")
        var interdescription = $(".inter-description").attr("data-description")
        var q1;
        var q2;
        var q3;
        var q4;
        var q5;
        var q6;
        if(document.getElementById("radio1").checked){
            q1 = document.getElementById("radio1").value;
        } else if(document.getElementById("radio2").checked){
            q1 = document.getElementById("radio2").value;
        }
        if(document.getElementById("radio3").checked){
            q2 = document.getElementById("radio3").value;
        } else if(document.getElementById("radio4").checked){
            q2 = document.getElementById("radio4").value;
        }
        if(document.getElementById("radio5").checked){
            q3 = document.getElementById("radio5").value;
        } else if(document.getElementById("radio6").checked){
            q3 = document.getElementById("radio6").value;
        }
        if(document.getElementById("radio7").checked){
            q4 = document.getElementById("radio7").value;
        } else if(document.getElementById("radio8").checked){
            q4 = document.getElementById("radio8").value;
        }
        if(document.getElementById("radio9").checked){
            q5 = document.getElementById("radio9").value;
        } else if(document.getElementById("radio10").checked){
            q5 = document.getElementById("radio10").value;
        }
        var e = document.getElementById("duration");
        q6 = e.options[e.selectedIndex].text;
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
        console.log(data)
        $.ajax({
        type: "POST",
        url: "/title_description",
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
});