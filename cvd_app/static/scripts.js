$(document).ready(function(){
  var result = $("#result");
  result.css('display', 'none');
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
        result.css('display', 'block');
        if (request_type == "POST") { // probs cleaner way to do this
          result.html(`${res}`);
        } else {
          result.html(`10 year cardiovascular risk: ${res.risk}%`);
        }
      },
      error:function(e){
        result.css('display', 'block');
        result.html("ERROR. Check python console output");
      }
    });
    event.preventDefault();
  });
});