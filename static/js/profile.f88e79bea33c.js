$(document).ready(function() {
    var editNameMode = true;
    $("#profile-totimeline").click(function() {
        clearAll();
        $("#profile-timeline").removeClass("hidden");
        $("#profile-totimeline").addClass("selected-button");
    })
    $("#profile-toquickinfo").click(function() {
        clearAll();
        $("#profile-quickinfo").removeClass("hidden");
        $("#profile-toquickinfo").addClass("selected-button");
    })
    $("#profile-torequests").click(function() {
        clearAll();
        $("#profile-requests").removeClass("hidden");
        $("#profile-torequests").addClass("selected-button");
    })

    addRequest();
    $("#changeNameMode").click(function() {
        editName(editNameMode);
        editNameMode = ! editNameMode;
    })

    var header_height = $("#profile-header").height();
    if(header_height > 0)
    {
      $(".content").css("margin-top",header_height);
    }

});

function submitUpdateNameForm() {
    document.getElementById('updatenameform').submit();
}

function submitUpdateRequestsForm() {
    document.getElementById('newrequestinput').submit();
}

function removeRequestForm() {
    document.getElementById('deleterequestform').submit();
}

function removeTagForm() {
    document.getElementById('deletetagform').submit();
}

function clearAll() {
    $("#profile-timeline").addClass("hidden");
    $("#profile-quickinfo").addClass("hidden");
    $("#profile-requests").addClass("hidden");
    $("#profile-totimeline").removeClass("selected-button");
    $("#profile-toquickinfo").removeClass("selected-button");
    $("#profile-torequests").removeClass("selected-button");
};

function addRequest() {
    $(addrequestbutton).click(function() {
        var newRequest = $(document.createElement('li'));
        newRequest.addClass("table-view-cell");
        var inputRequest = $(document.createElement(''))
        $("#requestlist").prepend(newRequest);
    })
};

function editName(editNameMode) {
    if (editNameMode) {
        $("#nameformdiv").removeClass("hidden");
        $("#namedisplaydiv").addClass("hidden");
        $("#tags").addClass("hidden");
        $("#changeNameMode").addClass("hidden");
    } else {
        $("#nameformdiv").addClass("hidden");
        $("#namedisplaydiv").removeClass("hidden");
        $("#tags").removeClass("hidden");
        $("#changeNameMode").removeClass("hidden");
    }
};