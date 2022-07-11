$(document).ready(function(){
        $(".overlay").on("click", function (e) {
        if (e.target !== this) {
            return;
        }
        $(".overlay").hide();
        });


})