//Data

//Definition Grafik

const gridOptions = {
    columnDefs: [
      { field: 'salesRep', chartDataType: 'category' },
      { field: 'handset', chartDataType: 'category' },
      { field: 'sale', chartDataType: 'series' },
      { field: 'saleDate', chartDataType: 'category' },
    ],
    defaultColDef: {
      flex: 1,
      sortable: true,
      filter: 'agSetColumnFilter',
      floatingFilter: true,
      resizable: true,
    },
    rowData: getData(),
    enableCharts: true,
    chartThemes: ['ag-default-dark'],
    onFirstDataRendered: onFirstDataRendered,
  };

//Grafik sales chart
function onFirstDataRendered(params) {
    params.api.createCrossFilterChart({
      chartType: 'pie',
      cellRange: {
        columns: ['salesRep', 'sale'],
      },
      aggFunc: 'sum',
      chartThemeOverrides: {
        common: {
          title: {
            enabled: true,
            text: 'Sales by Representative ($)',
          },
        },
        pie: {
          series: {
            title: {
              enabled: false,
            },
            label: {
              enabled: false,
            },
          },
        },
      },
      chartContainer: document.querySelector("sales-chart"),
    });
  }