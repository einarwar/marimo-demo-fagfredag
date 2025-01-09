import marimo

__generated_with = "0.10.9"
app = marimo.App(
    width="medium",
    layout_file="layouts/demo_notebook.slides.json",
)


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r""" """)
    return


@app.cell
def _(mo):
    mo.md(r"""# Star history""")
    mo.image("https://api.star-history.com/svg?repos=marimo-team/marimo,jupyter/notebook&type=Timeline")

    return


@app.cell
def _(mo):
    mo.md("#Hei")
    print(1+1)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
