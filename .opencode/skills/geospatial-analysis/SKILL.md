---
name: geospatial-analysis
description: Create maps and spatial visualizations for urban/regional data. Supports heatmaps, cluster maps, grid analysis, and interactive maps with Folium.
license: MIT
compatibility: opencode
metadata:
  domain: data-science
  tasks: [maps, spatial-analysis, geo-visualization, folium]
---

# Geospatial Analysis Skill

You are an expert in geospatial visualization and spatial analysis. Your goal is to help users create maps and analyze spatial patterns in their data.

## What I Do

### 1. Map Visualizations
- **Point maps** - Scatter points on geographic coordinates
- **Heatmaps** - Density visualization (lat/lon based)
- **Choropleth maps** - Region-based colored maps (if shapefile available)
- **Interactive HTML maps** - Folium-based zoomable maps

### 2. Spatial Analysis
- **Grid analysis** - Divide area into grids (e.g., 500m x 500m)
- **Hotspot detection** - Identify high-density areas
- **Cluster visualization** - Show spatial clustering patterns

### 3. Distance & Geometry Calculations
- **Haversine distance** - Calculate great-circle distance between two points
- **Bounding box** - Calculate geographic bounds of data
- **Centroid calculation** - Find geometric center of points
- **Nearest neighbor analysis** - Find closest points to each location

### 4. Advanced Clustering Algorithms
- **K-means clustering** - Partition points into k groups
- **DBSCAN** - Density-based spatial clustering
- **Hierarchical clustering** - Dendrogram-based grouping

### 5. Population & Concentration Analysis
- **Population concentration** - Calculate top N percentage of total
- **Regional aggregation** - Group by geographic regions
- **Density metrics** - Calculate points per unit area
- **Center of gravity** - Weighted center by population/value

### 3. Urban Data Visualization
- **POI density maps** - Points of interest distribution
- **Facility coverage** - Service area analysis
- **Grid statistics** - Aggregated metrics by grid cell

## When to Use Me

Use this skill when:
- User asks to "create a map" or "visualize geography"
- User mentions "spatial", "geo", "location", "lat", "lon"
- User wants "heatmap" of geographic data
- User asks for "grid analysis" or "spatial clustering"
- Data contains latitude/longitude coordinates
- User wants "interactive map" (HTML output)
- User asks for "distance calculation" or "Haversine"
- User asks for "population concentration" or "clustering"
- User needs "nearest neighbor" analysis

## Workflow

1. **Identify coordinates** - Find lat/lon columns in data
2. **Assess data** - Check coordinate ranges, coverage area
3. **Select method** - Recommend visualization approach
4. **Generate map** - Create static or interactive visualization
5. **Add context** - Add markers, labels, legends
6. **Save output** - HTML for interactive, PNG for static

## Coordinate Detection

Auto-detect common column names:
- `lat` / `latitude` / `Lat` / `Latitude`
- `lon` / `lng` / `longitude` / `Lon` / `Lng`
- `y` / `x` (when clearly geographic)

## Example Usage

```
Visualize Shanghai grid data:
- Create heatmap of population density
- Show business facility distribution
- Generate interactive map with markers
- Identify hotspots in the data

Calculate distances between locations:
- Compute Haversine distance between city centers
- Find nearest metro station for each district
- Calculate coverage radius for facilities

Analyze population concentration:
- Calculate top 10% cities population share
- Identify high-density urban clusters
- Find population-weighted centers
```

## Distance Calculation (Haversine)

```python
from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate great-circle distance between two points (km)"""
    R = 6371  # Earth radius in km
    
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    
    return R * c

# Usage
dist = haversine_distance(31.2304, 121.4737, 31.2304, 121.4737)  # Shanghai to itself
```

## Clustering Algorithms

```python
from sklearn.cluster import KMeans, DBSCAN
import numpy as np

def spatial_kmeans(coordinates, n_clusters=5):
    """K-means clustering for geographic data"""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(coordinates)
    return labels, kmeans.cluster_centers_

def spatial_dbscan(coordinates, eps_km=1, min_samples=5):
    """DBSCAN clustering - finds dense regions"""
    # Convert km to degrees (approximate)
    eps_deg = eps_km / 111  # 1 degree ≈ 111 km
    
    db = DBSCAN(eps=eps_deg, min_samples=min_samples, metric='euclidean')
    labels = db.fit_predict(coordinates)
    return labels
```

## Population Concentration Analysis

```python
def population_concentration(df, pop_column, top_n=10):
    """Calculate population concentration ratio"""
    sorted_data = df.sort_values(pop_column, ascending=False)
    
    total = sorted_data[pop_column].sum()
    top_n_sum = sorted_data[pop_column].head(top_n).sum()
    
    concentration = {
        'top_n_count': top_n,
        'top_n_share': top_n_sum / total * 100,
        'total_population': total,
        'top_n_population': top_n_sum,
        'gini_coefficient': calculate_gini(sorted_data[pop_column])
    }
    return concentration

def calculate_gini(values):
    """Calculate Gini coefficient for inequality"""
    sorted_values = np.sort(values)
    n = len(values)
    cumsum = np.cumsum(sorted_values)
    return (2 * np.sum((np.arange(1, n+1) * sorted_values)) - (n + 1) * np.sum(sorted_values)) / (n * np.sum(sorted_values))

def weighted_centroid(df, lat_col, lon_col, weight_col):
    """Calculate population-weighted center"""
    total_weight = df[weight_col].sum()
    center_lat = (df[lat_col] * df[weight_col]).sum() / total_weight
    center_lon = (df[lon_col] * df[weight_col]).sum() / total_weight
    return center_lat, center_lon
```

## Python Libraries

- pandas - Data manipulation
- folium - Interactive maps
- geopandas - Spatial data (if shapefiles needed)
- matplotlib - Static maps
- scipy.spatial - Spatial clustering
- sklearn.cluster - K-means, DBSCAN clustering
- numpy - Numerical operations

## Output

Provide:
1. **Map file** - HTML (interactive) or PNG (static)
2. **Coordinate summary** - Data coverage statistics
3. **Key insights** - Spatial patterns discovered
4. **Recommendations** - Further analysis suggestions
5. **Analysis results** - Distance matrices, cluster labels, concentration metrics (if calculated)
