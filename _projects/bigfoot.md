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
[The Analysis](https://github.com/RithvikM14/RithvikM14.github.io/blob/main/python_notebooks/bigfoot.py)
---

### 🌕 Sightings by Moon Phase and Season

This bar chart shows Bigfoot sightings binned by moon phase (0 = new moon, 1 = full moon), grouped by season. It explores whether moonlight and time of year influence sighting patterns.

The x-axis encodes **moon phase** (quantitative, binned), the y-axis encodes **count of sightings**, and color encodes **season** (nominal), again using a categorical palette.

Color helps show seasonal distribution within each moon phase bin. This enhances comparisons across different lighting conditions and times of year.

The data was filtered to exclude missing values for `moon_phase` or `season`, and Altair’s `bin` function was used to group moon phase into 10 intervals. No manual aggregation was needed.

<vegachart schema-url="{{ site.baseurl }}/assets/json/bigfoot-chart2.json" style="width: 100%"></vegachart>



### 📊 Bigfoot Sightings by State and Season

This grouped bar chart shows the number of Bigfoot sightings by U.S. state, broken down by season. It helps identify which states have higher reports and whether certain seasons see more activity.

The x-axis encodes **state** (nominal), and the y-axis encodes the **count of sightings** (quantitative). Season is encoded with **color**, using a categorical palette to distinguish between spring, summer, fall, and winter.

Color was chosen for season to make it easy to compare seasonal trends within each state. The categorical color scheme improves visual clarity across groups.

In Python, I grouped the data by `state` and `season` using `groupby()`, then counted sightings. No additional filtering or binning was required for this plot.

<vegachart schema-url="{{ site.baseurl }}/assets/json/bigfoot-chart1.json" style="width: 100%"></vegachart>


