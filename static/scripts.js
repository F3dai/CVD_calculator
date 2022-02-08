$(document).ready(function(){
  $("#form").submit(function(){
    $.ajax({
      url: "calculate", 
      data: $("#form").serialize(), 
      type: "GET", 
      dataType: 'json',
      success: function (res) {
        console.log(res.result);
        $("#result").html(JSON.stringify(res));
      },
      error:function(e){
        alert(JSON.stringify(e));
      }
    }); 
    return false;
  });
});
