# Interactive Analysis (project)

This script replaces static Matplotlib/Seaborn plots with interactive Plotly figures.

What changed
- `projectfile.py`: now uses Plotly to create interactive figures and saves them as HTML files in `outputs/`.
- `requirements.txt`: minimal list of dependencies.

How to run

1. Create a virtual environment (optional but recommended).
2. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

3. Put `cleaned_file.csv` next to `projectfile.py` (same directory).
4. Run:

```powershell
python projectfile.py
```

Outputs
- Interactive HTML files are saved into the `outputs/` folder created next to the script.

Notes
- If run in an environment without a browser (headless), the HTML files are still produced and can be opened locally.
- The script prints warnings if expected columns are missing but will run best with columns: `price`, `age`, `quantity`, `customer_id`, `gender`, `review_score`, `payment_method`.
