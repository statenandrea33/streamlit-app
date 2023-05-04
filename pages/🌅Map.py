import streamlit as st
import leafmap
import leafmap.foliumap as leafmap

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.title("Interactive Map")
st.write("To interact with this map you can either select one from the dropdown menu or enter a URL.")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)
    url = st.text_input('Enter URL:','')
with col1:

    m = leafmap.Map(locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)

    if url:
        m.add_tile_layer(url,'base',attribution=" ")
    else:
        m.add_basemap(basemap)

    m.to_streamlit(height=700)