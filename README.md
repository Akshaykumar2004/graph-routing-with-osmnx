# Graph Navigation Application

This is a graph based navigation application built using OSMnx and Matplotlib in Python.The project was developed as a part of an applied data structure course.

## Project Structure

```
├── main.py
└── src
    ├── App.py
    ├── MyGraph.py
    ├── utils.py
```

- `main.py` - Launches the application  
- `src` - Contains all source code
  - `App.py` - Main application logic
  - `MyGraph.py` - Custom graph data structure and algorithms
  - `utils.py` - Helper methods for working with OSMnx graphs

## Features  

The application allows users to:

- Find nearest POI (Point of Interest) like a hospital, restaurant etc from a source location
- Search for shortest path between two addresses by travel time 
- Plot the routes on matplotlib graphs

## Usage

To run the application:
### Step 1
```bash
gh repo clone Akshaykumar2004/graph-routing-with-osmnx
```

### Step 2
```bash
pip install -r requiremnts.txt
```
### Step 3
```bash
python main.py
```


It provides an interactive command line interface to use the features.

## Extending the application

Some ideas for extending the features:  

- Add more POI types - parks, schools etc  
- Filter POIs by properties like ratings, opening times etc   
- Compare routes by distance, cost etc    
- Add public transport routing
- Improve UI with better search, interactive maps etc  

## Libraries Used

- OSMnx - To download graph data from OpenStreetMap  
- Matplotlib - To plot the graph routes


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 


