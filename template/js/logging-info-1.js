// using jQuery Django
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
    csrftoken = getCookie('csrftoken');
    $("#log-inter").click(function(){
        var title = $(".inter-title").val();        
        var description = $(".inter-description").val();
        console.log("title"+title)
        console.log("description"+description)
        var data = {
            "title": title,
            "description": description
        };
        var clientID = $(".client-id").attr("data-cid");

        $.ajax({
        type: "POST",
        url: "/title_description/" + clientID,
        data: data,
        beforeSend: function (xhr) {
          xhr.withCredentials = true;
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function(data) {
            console.log(clientID)
            window.location.href = "/logging_info_2/" + clientID
        },
        async: true
      });
    })
});