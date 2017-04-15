var sub_page;// = "quick_info"

$(document).ready(function() {
    if (!sub_page) {
        sub_page = "quick_info"
        setPages();
    }
    $("#change_subpage_form").click(function() {
        changeSubPage();
    })
    sub_page = localStorage.getItem("sub_page");
    setPages();
});

function removeRequestForm() {
    document.getElementById('deleterequestform').submit();
}

function removeTagForm() {
    document.getElementById('deletetagform').submit();
}

function changeSubPage() {
    sub_page = $('input[name="sub_page"]:checked').val();
    setPages();
    localStorage.setItem("sub_page", sub_page);    
}

function setPages() {
    clearAll();
    switch(sub_page) {
        case "timeline": 
            $("#profile-timeline").removeClass("hidden");
            $("#profile-totimeline").addClass("selected-button");
            break;
        case "quick_info": 
            $("#profile-quickinfo").removeClass("hidden");
            $("#profile-toquickinfo").addClass("selected-button");
            break;
        case "requests": 
            $("#profile-requests").removeClass("hidden");
            $("#profile-torequests").addClass("selected-button");
            break;    
    }
}

function clearAll() {
    $("#profile-timeline").addClass("hidden");
    $("#profile-quickinfo").addClass("hidden");
    $("#profile-requests").addClass("hidden");
    $("#profile-totimeline").removeClass("selected-button");
    $("#profile-toquickinfo").removeClass("selected-button");
    $("#profile-torequests").removeClass("selected-button");
};


