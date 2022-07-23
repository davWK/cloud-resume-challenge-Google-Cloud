/*$(document).ready(function(){
    $.getJSON("https://us-central1-alilikpo-228.cloudfunctions.net/get_visitor_number", function(data){
        $("#visitor-count").text(data.count);
    }).fail(function(){
        console.log("An error has occurred while fetching the visitor count.");
    });
});

*/


$(document).ready(function(){
    $.getJSON("https://us-central1-alilikpo-228.cloudfunctions.net/get_visitor_number", function(data){
        $("#visitor-count").text(data.count);
        $('[data-toggle="counter-up"]').counterUp({
            delay: 10,
            time: 1000
        });
    }).fail(function(){
        console.log("An error has occurred while fetching the visitor count.");
    });
});
