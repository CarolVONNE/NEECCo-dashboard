# North East England Climate Coalition - Indicators Dashboard

# How NEECCo developed climate indicators

NEECCo – the North East England Climate Coalition - was formed in 2019, adopting the mission of “Becoming England’s Greenest Region”, with the aims of addressing the climate emergency and the ecological collapse while advocating for a just transition. If we were going to make such claims we needed to understand if as a region we were doing enough of the right things, fast enough (spoiler alert: we’re not yet). And so the Indicators Project was initiated.

During the development of the dashboard several hundred people have been involved –thanks to them all. Initial conversations with a wide range of people from across the region led to a mock up, paper version of the dashboard. The issues of creating an on-line resource were considered through a Hackathon organised with National Innovation Centre for Data – NICD - to coincide with the UN CoP 26 in Glasgow, and subsequently the Analysts Network North East 2022 Challenge. During the summer of 2022 a set of thematic expert roundtables helped to identify and shape the final content. The invaluable support and technical input from NICD has produced and populated the current visualisation.

Since its production the mock up has been discussed with multiple and diverse audiences. Consistently there have been two responses. People tend to say either “that’s interesting, I’d never thought about …”, or “yes but shouldn’t this (issue/data) also be included?”. So it has become clear that this resource is most useful for informing and enabling better conversations. Informed discussion is not enough, but it is necessary if we are to make the fundamental changes that are essential.

The project has been funded by NEECCo with specific support from Sage Group and the Environment Agency. NICD’s work has been funded by NEECCo and Sage Group, at a rate subsidized by the North of Tyne Combined Authority. The project was initiated by Claire Thompson and subsequently led by Chris Ford. The NICD team of Hollie Johnson and Louise Braithwaite was led by Peter Michalak. Thanks to them all.

If you would like to get in touch please email vonne@vonne.org.uk.

## Getting started

- Clone this repository
- Setup a virtual environment and install Python packages from [requirements.txt](./requirements.txt)
- Serve the Dash app in localhost mode from a command line:
```python
python index.py
```
- Once the server starts, go to [http://127.0.0.1:8085/](http://127.0.0.1:8085/) to view the dashboard.

## Technology

The visualisations for the dashboard are build using [Dash](https://dash.plotly.com/) framework in Python. We have used [Visual Studio Code](https://code.visualstudio.com/) as the IDE for the code development, and deployed using [Docker](https://www.docker.com/). The data processing tasks were carried out with standard packages, such as [Pandas](https://pandas.pydata.org/), [Numpy](https://numpy.org/), and for working with geospatial data [Folium](https://github.com/python-visualization/folium) package was used.

## Methodology

Each Indicator group has it's own README file under [Methodology](./methodology/) folder. These files list the indicators and link to the original data sources that were used for visualisations. Due to nature of the variety data sources, some needed preprocessing steps to make them easier to display on this dashboard. Methodology files link individual Python notebooks that were used to preprocess the data where necessary. For each indicator with a data source, the 'Reference in locations.json' entry lists a key that can be used to look-up the dataset that the dashboard loads.

**Locations.json file**

A reference [locations.csv](./locations.json) contains links to data files that are displayed on the dashboard. To update any of the existing entries replace the URL for the name of the data source.
Locations.json file is referred to throughout the [methodology sections](./methodology/) as this is used internally by the dashboard to load source data before plots are rendered.

## Build a Docker image 

### Build Docker image

To build a new Docker image run following command from the `dashboard` folder (`neecco-dash` is a name for the new docker container). During this step we inject a build argument into environment, this is loaded by the dashboard and displayed on the front page.

```
docker build --build-arg now="$(date +%Y-%m-%d_%H:%M)" -t neecco-dash .
```

### Tag Docker image
Tag the latest version for upload:

```
docker tag neecco-dash:latest neeccocontainerreg.azurecr.io/neecco-dash:latest
```

### Push image to a Container Register

Login and push the tagged image to a container registry of your choice. For this project we have used [DockerHub](https://hub.docker.com/).

## License

This work is licensed under: [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)