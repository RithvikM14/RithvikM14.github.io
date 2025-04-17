---
name: "Bigfoot Sightings Visualizations"
tools: [Python, HTML, altair]
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---

[The Data](https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/bfro_reports_fall2022.csv)  
[The Analysis](https://github.com/RithvikM14/RithvikM14.github.io/blob/main/python_notebooks/Rithvik-HW-5.2.ipynb)
---

## 🗺️ Map of Bigfoot Sightings with Weather Conditions

This map displays the locations of reported Bigfoot sightings across the U.S., with color representing the moon phase at the time of each sighting. Users can filter sightings using a dropdown menu for each state. This interactivity helps highlight spatial clusters and potential atmospheric patterns in the sightings.

We can use a vegachart HTML tag like so:

```
<vegachart schema-url="{{ site.baseurl }}/assets/json/cars.json" style="width: 100%"></vegachart>
```

<vegachart schema-url="https://github.com/RithvikM14/RithvikM14.github.io/blob/main/assets/json/bigfoot-chart2.json" style="width: 100%"></vegachart>



## 📊 Sightings by State and Season

This grouped bar chart shows the number of Bigfoot sightings in each state across all four seasons. It gives a clear breakdown of seasonal trends in each region, highlighting whether reports spike during certain times of the year.

<vegachart schema-url="https://github.com/RithvikM14/RithvikM14.github.io/blob/main/assets/json/bigfoot-chart1.json" style="width: 100%"></vegachart>


