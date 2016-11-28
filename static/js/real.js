var data_dolar = []

function week_real(week_currency) {
    data_dolar = week_currency.reverse()
}


$(function () {
          Highcharts.chart('real', {
             chart: {
                zoomType: 'x',

                 backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 1, y2: 1 },
                    stops: [
                    [0, 'rgba(43, 43, 44, 0.4)'],
                    [1, 'rgba(62, 62, 65, 0.4)']
                    ]
                },
                 plotBorderColor: '#606063'

            },

            title: {
                text: 'USR to BRL exchange rate over time',
                style: {
                 color: '#E0E0E3',
                 fontSize: '20px'
                 }
            },
            subtitle: {
                text: document.ontouchstart === undefined ?
                        'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in',
                style: {
                    color: '#E0E0E3',
                 }
            },
          
            xAxis: {
               categories: ['Dia 01', 'Dia 02', 'Dia 03', 'Dia 04', 'Dia 05', 'Dia 06',
                'Hoje'],
                gridLineColor: '#707073',
                labels: {
                    style: {
                    color: '#E0E0E3'
                    }
                },
                lineColor: '#E0E0E3',
                minorGridLineColor: '#505053',
                tickColor: '#E0E0E3',
                title: {
                    style: {
                        color: '#A0A0A3'

                    }
                }
            },
            yAxis: {
                  gridLineColor: '#E0E0E3',
                  labels: {
                     style: {
                        color: '#E0E0E3'
                     }
                  },
                  color: '#E0E0E3',
                  minorGridLineColor: '#505053',
                  tickColor: '#707073',
                  tickWidth: 1,
                  title: {
                     style: {
                        color: '#E0E0E3'
                     }
                  }
               },

            legend: {
                enabled: false
            },

            plotOptions: {
                area: {
                    fillColor: {
                        linearGradient: {
                            x1: 0,
                            y1: 0,
                            x2: 1,
                            y2: 1
                        },
                        stops: [
                            [0, 'rgba(43, 43, 44, 0.9)'],
                            [1, 'rgba(62, 62, 65, 0.9)']
                        ]
                    },
                    marker: {
                        radius: 2
                    },
                    lineWidth: 1,
                    states: {
                        hover: {
                            lineWidth: 1
                        }
                    },
                    threshold: null
                },
                series: {
                    marker: {
                        lineColor: '#white'
                    },
                    dataLabels: {
                    color: '#white'
                    }
                },
            },

            series: [{
                type: 'area',
                color: '#E0E0E3',

                name: 'BRL to USD',
                data: data_dolar
            }]
        });
    });