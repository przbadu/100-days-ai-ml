# California House Price Prediction Model

## Model Information
- Algorithm: Random Forest Regressor
- Features: 8 original + 7 engineered features
- R² Score (Test): {best_rf_test_r2:.4f}
- RMSE (Test): {best_rf_test_rmse:.4f}
- Mean Absolute Percentage Error: 19.04%

## Features Used
Original Features:
- MedInc: Median income in block group
- HouseAge: Median house age in block group
- AveRooms: Average number of rooms
- AveBedrms: Average number of bedrooms
- Population: Block group population
- AveOccup: Average house occupancy
- Latitude: Block group latitude
- Longitude: Block group longitude

Engineered Features:
- Income_Location
- Rooms_per_Household
- Bedrooms_per_Room
- Population_per_Household
- MedInc_Log
- Population_Log
- AveOccup_Log

## Limitations and Assumptions
1. Geographic Limitation: Model trained only on California housing data
2. Time Period: Data from 1990s California housing market
3. Price Range: Model may be less accurate for extremely low or high prices
4. Feature Constraints: All input features must be provided and within training data range

## Usage Guidelines
1. Input values should be within similar ranges as training data
2. Predictions are in 100k units (multiply by 100000 for dollar value)
3. Model should be periodically retrained with newer data