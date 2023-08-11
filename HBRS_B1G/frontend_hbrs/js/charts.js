import ApexCharts from 'apexcharts'

  var options = {
    chart: {
      type: 'bar'
    },
    series: [{
      name: 'Sales',
      data: [30, 40, 45, 50, 49, 60, 70, 91, 125]
    }],
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
    }
  }

  var chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();

