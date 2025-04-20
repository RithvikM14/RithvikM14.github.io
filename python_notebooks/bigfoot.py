import pandas as pd
import altair as alt

# Allow large datasets
alt.data_transformers.disable_max_rows()

# Load the data
url = 'https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/bfro_reports_fall2022.csv'
df = pd.read_csv(url)

# -------------------------------
# PLOT 1: Sightings by State and Season
# -------------------------------

# Group sightings by state and season
df_plot1 = df.groupby(['state', 'season']).size().reset_index(name='count')

chart1 = alt.Chart(df_plot1).mark_bar().encode(
    x=alt.X('state:N', sort='-y', title='State'),
    y=alt.Y('count:Q', title='Number of Sightings'),
    color=alt.Color('season:N', title='Season'),
    tooltip=['state:N', 'season:N', 'count:Q']
).properties(
    width=700,
    height=400,
    title='Bigfoot Sightings by State and Season'
).interactive()

chart1.properties(width='container').save("/Users/rithvikmandumula/RithvikM14.github.io/assets/json/bigfoot-chart1.json")

# -------------------------------
# PLOT 2
# -------------------------------

# Create a new column with binned moon phases (e.g. 0.0 to 1.0 in steps of 0.2)
df_moon = df.dropna(subset=['moon_phase', 'season'])  # clean missing data

chart_moon = alt.Chart(df_moon).mark_bar().encode(
    x=alt.X('moon_phase:Q', bin=alt.Bin(maxbins=10), title='Moon Phase (binned)'),
    y=alt.Y('count():Q', title='Number of Sightings'),
    color=alt.Color('season:N', title='Season'),
    tooltip=[
        alt.Tooltip('count():Q', title='Sightings'),
        alt.Tooltip('season:N'),
        alt.Tooltip('moon_phase:Q', bin=True)
    ]
).properties(
    width=700,
    height=400,
    title='Bigfoot Sightings by Moon Phase and Season'
)


# Final layered chart with zoom & hover
chart_moon.properties(width='container').save("/Users/rithvikmandumula/RithvikM14.github.io/assets/json/bigfoot-chart2.json")
