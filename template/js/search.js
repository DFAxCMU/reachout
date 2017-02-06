$(document).ready(function() {
    var header_height = $("#search-header").height();
    if(header_height > 0) {
      $(".content").css("margin-top", header_height);
    }
});
