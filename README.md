# ObjectDetection

Object Detection using YOLOv3
  
## Installation guide

Please read [installation.md](installation.md) for details on how to set up this project.

## Project Organization

    ├── LICENSE
    ├── tasks.py           <- Invoke with commands like `notebook`.
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │                     the creator's initials, and a short `-` delimited description
    │   └── 0.0-example-data-exploratory.ipynb  <- Example notebook ready to be used as script
    │   └── 1.0-Mateo Gravi Fiorino-data-cleaning.ipynb                        
    │   └── 2.0-Mateo Gravi Fiorino-data-exploration.ipynb                        
    │   └── 2.0-Mateo Gravi Fiorino-data-preprocessing.ipynb                        
    │   └── 2.0-Mateo Gravi Fiorino-feature-selection.ipynb                        
    │   └── 2.0-Mateo Gravi Fiorino-model-training.ipynb                        
    │   └── 2.0-Mateo Gravi Fiorino-model-evaluation-and-optimization.ipynb                        
    │   └── 2.0-Mateo Gravi Fiorino-monitoring-and-maintenance.ipynb   
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so test can be imported.
    │
    └── test               <- Source code for use in this project.
        ├── __init__.py    <- Makes test a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts to help with common tasks.
            └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py

---
Project based on the [cookiecutter-ds](https://github.com/royquillca/cookiecutter-ds).