$(document).ready(function(){
  $("#form input[type=submit]").click(function(event){
    var option = $(this).val();
    // Determine which button clicked and request type
    if (option == "calculate") {
      var request_type = "GET";
    }
    else {
      var request_type = "POST";
    }
    $.ajax({
      url: "calculate", 
      data: $("#form").serialize(), 
      type: request_type, 
      dataType: 'json',
      success: function (res) {
        console.log(`Successful ${request_type} request. Data: ${res.result}`);
        $("#result").html(JSON.stringify(res));
      },
      error:function(e){
        alert(JSON.stringify(e));
      }
    });
    event.preventDefault();
  });
});