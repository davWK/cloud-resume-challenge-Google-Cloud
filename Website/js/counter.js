$(document).ready(function(){
    $.getJSON("https://us-central1-alilikpo-228.cloudfunctions.net/get_visitor_number", function(data){
        $("#visitor-count").text(data.count);
    }).fail(function(){
        console.log("An error has occurred while fetching the visitor count.");
    });
});
