$(function () {
    var myChart = Highcharts.chart('container', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Weekly Temperature Evaluation'
        },
        xAxis: {
            type: 'datetime',
            title: {
                text: 'Date/Time'
            }
        },
        yAxis: {
            title: {
                text: 'Temp Value'
            }
        },
        series: [{ }]

    });
});


//$(function () {
//    $.getJSON('http://127.0.0.1:8000/ground_zero/data/jsonp.php?filename=range.json&callback=?', function(data) {
//
//    	$('#container').highcharts({
//
//		    chart: {
//		        type: 'spline'
//		    },
//
//		    title: {
//		        text: 'Temperature variation by day'
//		    },
//
//		    xAxis: {
//		        type: 'datetime'
//		    },
//
//		    yAxis: {
//		        title: {
//		            text: null
//		        }
//		    },
//
//		    tooltip: {
//		        crosshairs: true,
//		        shared: true,
//		        valueSuffix: '°C'
//		    },
//
//		    legend: {
//		        enabled: false
//		    },
//
//		    series: [{
//
//		    }]
//
//		});
//    });
//
//});