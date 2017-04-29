var sub_page;

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

    $('#successMessage').delay(500).fadeOut('slow');
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
            break;
        case "quick_info": 
            $("#profile-quickinfo").removeClass("hidden");
            break;
        case "requests": 
            $("#profile-requests").removeClass("hidden");
            break;    
    }
}



function clearAll() {
    $("#profile-timeline").addClass("hidden");
    $("#profile-quickinfo").addClass("hidden");
    $("#profile-requests").addClass("hidden");
};


