function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
$(document).ready(function () {
  $("#songform").submit(function (e) {
    e.preventDefault();
    var formData = new FormData(this);
    var url = $(this).data('url')
    $.ajax({
      url: url,
      type: "POST",
      data: formData,

      success: function (data) {
        console.log("success"); // ... do something with the data...
      },
      cache: false,
      contentType: false,
      processData: false,
    });
  });


  
     $("#modelbutton").click(function () {
       $("#exampleModal").modal("show");
     });

     $("#artistform").submit(function (e) {
       e.preventDefault();
       var formdata = $("#artistform").serializeArray();
       formdata.push({
         name: "csrfmiddlewaretoken",
         value: getCookie("csrftoken"),
       });
       var url = $(this).data('url')
       $.ajax({
         url: url,
         type: "post",
         data: formdata,
         success: function (response) {
           $("#exampleModal").modal("hide");
           console.log(response["id"]);
         },
       });
     });
   
});
