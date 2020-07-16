am4core.ready(function() {
am4core.useTheme(am4themes_animated);

// Create map instance
var chart = am4core.create("chartdiv", am4maps.MapChart);
chart.geodata = am4geodata_usaLow;
chart.projection = new am4maps.projections.Miller();

// Create map polygon series for country` map
var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
var polygonTemplate = polygonSeries.mapPolygons.template;
polygonSeries.useGeodata = true;
polygonSeries.exclude = ["US-AK", "US-HI"];
polygonSeries.heatRules.push({
    property: "fill",
    target: polygonTemplate,
    min: am4core.color('#FFFFFF').brighten(-.1),
    max: am4core.color('#000000'),
});

polygonTemplate.adapter.add("tooltipHTML", function(text, mPolygon) {
    poly_data = mPolygon.dataItem.dataContext;
    output_text = ''
    if (poly_data['winner']){ // Senate results exist
        output_text = `<center><strong>{name}</strong></center>
        <hr />
        <table>
        <tr>
            <th align="left" style="padding: 5px">{winner}</th>
            <td style="padding: 5px">{topvotepercent.formatNumber('###.##')}</td>
        </tr>
        <tr>
            <th align="left" style="padding: 5px">{loser}</th>
            <td style="padding: 5px">{secondvotepercent.formatNumber('###.##')}</td>
        </tr>
        </table>`;
    } else {
        output_text = `<center><strong>{name}</strong></center>
        <hr />
        No Election`;
    }
    return output_text;
});

polygonTemplate.nonScalingStroke = true;
polygonTemplate.strokeOpacity = 0.5;
polygonTemplate.fill = am4core.color("#eee");
polygonTemplate.propertyFields.fill = "color";

polygonSeries.dataSource.url = '/static/money_vis/state_json_data.json';

// function to get data per year
function generate_parsing_adapter(year) {
    return function(data, target) {
        var new_data = []; 
        console.log('Adapting');
        data = data[year];
        for (var i = 0; i < data.length; i++){
            var row = data[i];
            curr_id = 'US-' + row['state']
            new_data.push({id: curr_id,
                           value: row['votepercentdifference'],
                           winner: row['winner'],
                           loser: row['loser'],
                           topvotepercent: row['topvotepercent'],
                           secondvotepercent: row['secondvotepercent']});
        }
        return new_data;
    };
};

polygonSeries.dataSource.adapter.add('parsedData', generate_parsing_adapter('1980'));

polygonSeries.dataSource.events.on("error", function(ev) {
    console.log('Parsing Error');
});

polygonSeries.dataSource.events.on("parseended", function(ev){
    console.log('parse ended');
});

polygonTemplate.adapter.add("fill", function(fill, mapPolygon) {
    console.log("Adapting fill");
    var data_ctx = mapPolygon.dataItem.dataContext;
    if (!data_ctx) {
        return fill;
    }
    if (!('winner' in data_ctx)){
        return fill
    }
    var winner = mapPolygon.dataItem.dataContext['winner'];
    if (winner === 'republican'){
        fill = am4core.color({'r':255, 'b':fill.rgb['b'], 'g':fill.rgb['g']});
    } else if (winner === 'democrat') {
        fill = am4core.color({'r':fill.rgb['r'], 'b':255, 'g':fill.rgb['g']});
    } else {
        fill = am4core.color({'r':fill.rgb['r'], 'b':fill.rgb['b'], 'g':255});
    }
    return fill;
})

//document.getElementById('filter').addEventListener('change', function(e) {
document.getElementById('filter').addEventListener('input', function(e) {
    polygonSeries.dataSource.adapter.remove('parsedData');
    polygonSeries.dataSource.adapter.add('parsedData', generate_parsing_adapter(e.target.value));
    polygonSeries.dataSource.load();
});

/*
polygonSeries.events.on("beforedatavalidated", function(ev) {
    var source = ev.target.data;
    var data = [];
    var test = source;
    console.log("Doing the thing");
    console.log(source);
    for(var i = 0; i < source.length; i++){
        var row = source[i];
        if (!(row['id'].startsWith('US-'))){
            data.push({id: 'US-' + row['id'], value: row['value']});
        } else {
            data.push(row);
        }
    }
    ev.target.data = data;
});
*/


var hs = polygonTemplate.states.create("hover");
hs.properties.fill = chart.colors.getIndex(9);



// Create country specific series (but hide it for now)
/*
var countrySeries = chart.series.push(new am4maps.MapPolygonSeries());
countrySeries.useGeodata = true;
countrySeries.hide();
countrySeries.geodataSource.events.on("done", function(ev) {
  worldSeries.hide();
  countrySeries.show();
});

var countryPolygon = countrySeries.mapPolygons.template;
countryPolygon.tooltipText = "{name}";
countryPolygon.nonScalingStroke = true;
countryPolygon.strokeOpacity = 0.5;
countryPolygon.fill = am4core.color("#eee");

var hs = countryPolygon.states.create("hover");
hs.properties.fill = chart.colors.getIndex(9);
*/

// Set up click events
/*
usPolygon.events.on("hit", function(ev) {
  ev.target.series.chart.zoomToMapObject(ev.target);
  var map = ev.target.dataItem.dataContext.map;
  if (map) {
    ev.target.isHover = false;
    countrySeries.geodataSource.url = "https://www.amcharts.com/lib/4/geodata/json/" + map + ".json";
    countrySeries.geodataSource.load();
  }
});
*/

// Set up data for countries
/*
var data = [];
for(var id in am4geodata_data_countries2) {
  if (am4geodata_data_countries2.hasOwnProperty(id)) {
    var country = am4geodata_data_countries2[id];
    if (country.maps.length) {
      data.push({
        id: id,
        color: chart.colors.getIndex(continents[country.continent_code]),
        map: country.maps[0]
      });
    }
  }
}
worldSeries.data = data;
*/

// Zoom control
chart.zoomControl = new am4maps.ZoomControl();

var homeButton = new am4core.Button();
homeButton.events.on("hit", function() {
  worldSeries.show();
  countrySeries.hide();
  chart.goHome();
});

homeButton.icon = new am4core.Sprite();
homeButton.padding(7, 5, 7, 5);
homeButton.width = 30;
homeButton.icon.path = "M16,8 L14,8 L14,16 L10,16 L10,10 L6,10 L6,16 L2,16 L2,8 L0,8 L8,0 L16,8 Z M16,8";
homeButton.marginBottom = 10;
homeButton.parent = chart.zoomControl;
homeButton.insertBefore(chart.zoomControl.plusButton);

}); // end am4core.ready()
