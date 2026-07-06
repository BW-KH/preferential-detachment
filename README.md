# Source data & code for the main-text figures

`reproduce_figures.ipynb` reads the plotted values in `figure_data/` (and the
synthetic percolation runs in `simulation_data/`) and redraws every main-text
panel — Figure 1, Figure 2 and Figure 3 — into `Figures/`.

```bash
jupyter nbconvert --to notebook --execute reproduce_figures.ipynb
```

Requires Python 3 with numpy, pandas, scipy and matplotlib.

## Contents

* `figure_data/` — one text file per empirical panel (4 domains × Figure 1 A1–A3
  and Figure 2 B1–B3); each holds only that panel's plotted values.
* `simulation_data/` — synthetic network percolation runs behind Figure 3.
* `reproduce_figures.ipynb` — reads the above and reproduces every panel with the
  paper's exact styling.
* `binning.py` — helper used by the notebook.
