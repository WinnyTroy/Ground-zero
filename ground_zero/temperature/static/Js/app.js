//$(function () {
//    var myChart = Highcharts.chart('container', {
//        chart: {
//            type: 'spline'
//        },
//        title: {
//            text: 'Weekly Temperature Evaluation'
//        },
//        xAxis: {
//            type: 'datetime',
//            title: {
//                text: 'Date/Time'
//            }
//        },
//        yAxis: {
//            title: {
//                text: 'Temp Value'
//            }
//        },
//        series: [{  }]
//
//    });
//});


$(function () {
    Highcharts.chart('container', {
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
            data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
        }]
    });
});



