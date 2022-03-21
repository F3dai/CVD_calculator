
// Reset graph when replacing values
function resetCanvas() {
  $('#graph').remove()
  $('#result-graph').append('<canvas id="graph"></canvas>')
}

// Draw graph
function graph(result, average) {
  if (result == ">=30") {
    result = "30";
  }
  else if (result == "<1") {
    result = "1";
  }
  const cvd_chart = new Chart(document.getElementById('graph'), {
    type: 'bar',
    data: {
      labels: ['Your Risk', 'Average'],
      datasets: [{
        label: 'CVD Risk',
        data: [result, average],
        backgroundColor: [
          'green',
          'orange',
        ],
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: "10 year CVD risk %"
          }
        },
        x: {
          title: {
            display: true,
            text: "Results"
          }
        }
      }
    }
  });
  return cvd_chart;
}

// Form handling
$(document).ready(function () {
  var resultBox = $('#result-box'); // result
  var resultCanvas = $('#result-graph') // comp chart
  resultBox.css('display', 'none');
  resultCanvas.css('display', 'none');
  $("#form").submit(function (event) {
    var serialised = $("#form").serialize();
    resetCanvas(); // Remove and add to clear canvas

    if (serialised.indexOf("nhs") >= 0) {
      var request_type = "POST";
    } else {
      var request_type = "GET";
    }

    $.ajax({
      url: "calculate",
      data: serialised,
      type: request_type,
      dataType: 'json',
      success: function (res) {
        resultBox.css('display', 'block'); // unhide res box
        if (res.status == "error") {
          resultCanvas.css('display', 'none');
          resultBox.html(`${res.message}`);
        } else {
          resultBox.html(res.message);
          if (request_type == "GET") {
            graph(res.message.risk, res.message.average); // draw chart
            resultCanvas.css('display', 'block'); // Unhide chart
            resultBox.html(`10 year risk: ${res.message.risk}%`);
          } else if (request_type == "POST") {
            console.log(res);
            graph(res.message.risk, res.message.average); // draw chart
            resultCanvas.css('display', 'block'); // Unhide chart
            resultBox.html(`10 year risk: ${res.message.risk}% <br>Patient record update: ${res.message.result}`);

          }
        }
        // if (request_type == "POST") { // probs cleaner way to do this
        //   resultBox.html(`${res}`);
        // } else {
        //   graph(res.risk, res.average); // draw chart
        //   resultCanvas.css('display', 'block'); // Unhide chart
        //   resultBox.html(`10 year risk: ${res.risk}%`);
        // }
      },
      error: function () {
        resultBox.css('display', 'block');
        $("result-box").html("error - Check python console output");
      }
    });
    event.preventDefault();
  });
});

// disabling form submissions if there are invalid fields
(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()