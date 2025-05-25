# Machine Learning for Water Quality Assessment: Predicting Potability and Proposing a Low-Cost Measuring Kit for Rural Uzbekistan

Welcome to an open-source repository providing source code for the paper:

> **Machine Learning for Water Quality Assessment:
Predicting Potability and Proposing a Low-Cost Measuring
Kit for Rural Uzbekistan**  
> by *Artyom Tashyan, Sarvar Bazarov, Samanbek Erkinov*


**Important Files and Directories**:

- **`data/`**: Data used to train the model
- **`graphs/`**: Files of graphs generated in `.ipynby` file
- **`model/`**: Contains notebook with data analysis scripts and 3 models (HistGradientBoosting, XGBoost, RandomForest) to predict whether water is potable or not; Additionally contains saved file of the model
- **`gui.py`** File with simple GUI for more comfortable model interference
---

## Installation

If you plan to run it locally, follow this guide:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/sqdArtemy/water_quality_analysis
    cd water_quality_analysis
    ```

2. **Set Up a Virtual Environment and installing dependencies**:

    ```bash
    uv sync
    ```
    Activate the environment:
    - **Unix/Linux/MacOS**:
        ```bash
        source .venv/bin/activate
        ```
    - **Windows**:
        ```bash
        .venv\Scripts\activate
        ```

    All the dependencies can be observed in the file `pyproject.toml`

## Start the script
1) **Run the model.ipynb**:
    - After previous steps are completed, you can run the Jupyter notebook. When everything is executed, you are able to observe data analysis and the results of the model interference.
    If you have any other dataset you can easily use it with the minimal changes to the code.
    P.S. All the graphs are saved to the `./graphs` directory.

2) **Run the gui.py**
    - By running this file you can access simple GUI for model interference on the URL: `localhost:8050`
    - To run, use this command:
        ```bash
        uv run gui.py
        ```

---

## Data analysis graphs

### Data Correlation Matrix
![Data Correlation Matrix](./graphs/correlation_matrix.png)

### Feature Distribution
![Feature Distribution](./graphs/feature_distributions.png)

## Model results

### Accuracy comparison
![Accuracy comparison](./graphs/model_accuracy_by_columns.png)

### F1-score comparison
![F1-score comparison](./graphs/best_model_f1_scores.png)

### Confusion matrices
#### Confusion matrix Random Forest
![Confusion matrix RF](./graphs/confusion_matrix_RandomForest.png)

#### Confusion matrix HistGradientBoosting
![Confusion matrix HistGradientBoosting](./graphs/confusion_matrix_HistGradientBoosting.png)

#### Confusion matrix XGBoost
![Confusion matrix XGBoost](./graphs/confusion_matrix_XGBoost.png)

---


## Contact

For questions or feedback, please contact us: 
[Artyom Tashyan](mailto:sqd.artemy@gmail.com),
[Sarvar Bazarov](mailto:s.bazarov@student.inha.uz)
[Samobek Erkinov](mailto:s.erkinov2@student.inha.uz)

