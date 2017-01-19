//function that receives the data from my views and models it such that it can be used in my templates
function get_temp( data ){

  var data={"firstName":"Ray"};
  document.getElementById("container1").innerHTML=data.firstName;

console.log(item);


}

$(function () {
    Highcharts.chart('container', {

        chart: {
            type: 'spline'
        },
        title: {
            text: 'Weekly Temperature Evaluation',
            x: -20 //center
        },
        xAxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        },
        yAxis: {
            title: {
                text: 'Temperature (°C)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: '°C'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: 'Temp',
            data: [ ]
        }]
    });
});





