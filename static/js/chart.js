$.ajax({
  url: $("#issue").attr("data-url"),
  dataType: 'json',
  success: function(data) {
    Highcharts.chart('issue', data);
  }
})
$.ajax({
  url: $("#status").attr("data-url"),
  dataType: 'json',
  success: function(data) {
    Highcharts.chart('status', data);
  }
})
$.ajax({
  url: $("#urgent").attr("data-url"),
  dataType: 'json',
  success: function(data) {
    Highcharts.chart('urgent', data);
  }
})
$.ajax({
  url: $("#noturgent").attr("data-url"),
  dataType: 'json',
  success: function(data) {
    Highcharts.chart('noturgent', data);
  }
});