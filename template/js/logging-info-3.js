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
    $("#log-qinfo").click(function(){
        var item_name = $(".item-box").val();        
        var e = document.getElementById("amount");
        var amount = e.options[e.selectedIndex].text;
        console.log("ayy"+item_name)
        console.log("Ayy"+amount)
        var data = {
            amount:amount,  
            item_name:item_name,
        };
        var clientID = $(".client-id").attr("data-cid");
        
        $.ajax({
        type: "POST",
        url: "/log_all_info/"+clientID,
        data: data,
        beforeSend: function (xhr) {
          xhr.withCredentials = true;
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function(data) {
            window.location.href = "/search"
        },
        async: true
        });
    });
});