$(document).ready(function(){
    $.getJSON("https://us-east1-coffeetime-dev-282015.cloudfunctions.net/cloudresume-visitor-count", function(data){
        $("#visitor-count").text(data.currentVisitor);
        $('[data-toggle="counter-up"]').counterUp({
            delay: 10,
            time: 1000
        });
    }).fail(function(){
        console.log("An error has occurred while fetching the visitor count.");
    });
});
