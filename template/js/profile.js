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


});

function submitUpdateNameForm() {
    console.log("submitting name form")
    document.getElementById('updatenameform').submit();
}

function submitUpdateRequestsForm() {
    console.log("submitting (add) request form")
    document.getElementById('newrequestinput').submit();
}

function removeRequestForm() {
    console.log("remove request")
    document.getElementById('deleterequestform').submit();
}

function removeTagForm() {
    console.log("remove tag")
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
        console.log("remove compose");
        $("#nameformdiv").removeClass("hidden");
        $("#namedisplaydiv").addClass("hidden");
        $("#tags").addClass("hidden");
        $("#changeNameMode").addClass("hidden");
        // $("#changeNameMode").removeClass("icon-compose");
        // $("#changeNameMode").addClass("icon-check");
    } else {
        console.log("add compose");
        $("#nameformdiv").addClass("hidden");
        $("#namedisplaydiv").removeClass("hidden");
        $("#tags").removeClass("hidden");
        $("#changeNameMode").removeClass("hidden");
        // $("#changeNameMode").addClass("icon-compose");
        // $("#changeNameMode").removeClass("icon-check");
    }
};