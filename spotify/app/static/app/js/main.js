$(document).ready(function(){
    $(".stars").on("click", '.rate', function(event){

        event.preventDefault();
        var content = ` `;
        var id = $(this).data("id");
        var parent_id = $(this).parent().attr("id");
        var rate_id= $(this).parent().data("rate_id");
        var url = $(this).parent().data("url");
        
        url = url.replace("@", id);
        $.ajax({
          type: "GET",
          url: url,
          dataType: "json",
          data: {
            
          },
          success: function (response) {
            for (var i = 1; i <= 5; i++) {
              if (i <= id) {
                content =
                  content +
                  `<span  class="fa fa-star fa-lg checked rate" data-id =` +
                  i +
                  `></span> `;
              } else {
                content =
                  content +
                  `<span  class="fa fa-star fa-lg rate" data-id =` +
                  i +
                  `></span> `;
              }
            }
            $("#" + parent_id).html(content);          
          },
        });




        
    })
    

})