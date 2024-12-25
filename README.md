[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Yi0Zbe2y)
# MAST30034 Project 1 README.md
- Name: Ngoc Minh Vu
- Student ID: 1375708

**Research Goal:** My research goal is estimating Uber surge pricing in NYC

**Timeline:** The timeline for the research area is 6 months from Dec 2023 - May 2024

Please run the `requirements.txt` file to download all the required libraries

To run the pipeline, please visit the `scripts` directory and run the file:
1. `download.py`: This downloads the raw data, including TLC data, weather data, and taxi_zones into the `data/landing` directory.

After that, please visit the `notebooks` and run the files in order:
1. `weather_preprocessing.ipynb`: This will do the preprocessing for weather data and store it in `data/raw`
2. `tlc_preprocessing.ipynb`: This will do the preprocessing for TLC data, merge with weather data and store it in `data/curated`
3. `prelimninary.ipynb`: This will produce several plots, stored in `plots/` to use in the Preliminary Analysis part 
4. `model.ipynb`: This will contain 2 models: LR and GBT, after that it will merge the predictions to test dataset and store in `data/curated`
5. `analyzing.ipynb`: This will produce several plots and analysis using in Discussion part