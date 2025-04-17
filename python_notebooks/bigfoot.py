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
)

chart1.properties(width='container').save("/Users/rithvikmandumula/RithvikM14.github.io/assets/json/bigfoot-chart1.json")

# -------------------------------
# PLOT 2: Interactive Map with Weather Info
# -------------------------------

from vega_datasets import data

# Drop rows with missing coordinates
df_map = df.dropna(subset=['latitude', 'longitude'])

# --- Create dropdown with "All" option ---
states = sorted(df_map['state'].dropna().unique().tolist())
states.insert(0, 'All')  # Add 'All' to top

# Create dropdown binding and selection
state_dropdown = alt.binding_select(options=states, name='Select State: ')
state_select = alt.param(name='SelectedState', bind=state_dropdown, value='All')

# US States background map
us_states = alt.topo_feature(data.us_10m.url, 'states')

background = alt.Chart(us_states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project('albersUsa').properties(
    width=700,
    height=400
).interactive()

# Bigfoot sightings points
points = alt.Chart(df_map).mark_circle(size=60).encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    color=alt.Color('moon_phase:Q', scale=alt.Scale(scheme='purplebluegreen'), title='Moon Phase'),
    tooltip=[
        'location:N', 'state:N', 'season:N', 
        'temperature_mid:Q', 'cloud_cover:Q', 
        'humidity:Q', 'summary:N'
    ]
).add_params(
    state_select
).transform_filter(
    "SelectedState === 'All' || datum.state === SelectedState"
)

# Combine base map + points
final_chart = background + points
final_chart.properties(width='container').save("/Users/rithvikmandumula/RithvikM14.github.io/assets/json/bigfoot-chart2.json")
