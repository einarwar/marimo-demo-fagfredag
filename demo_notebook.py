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
    mo.image("./assets/forside.png")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Agenda

        * Hva er en notebook?
        * Hva er Marimo, og hva gjør de anderledes?
        * Demo
        """
    ).left()
    return


@app.cell
def _(mo):
    mo.md(
        """
        # Hva er en notebook?
        * Interaktiv verktøy for koding. 
        * Fleksibel, celle-basert innholdsstruktur
        * Kombinere tekst og kode
        * Bruksområder:
            * Dataanalyse og visualisering
            * Prototyping
        """
    )
    return


@app.cell
def _(mo):
    img = mo.image(
        "https://aquaticarts.com/cdn/shop/products/Large-Marimo-Fertilizer-p1_1800x1800.jpg?v=1569107015",
        width=400,
        height=250,
    ).right()
    text = mo.md(
        """
        # Hva er Marimo?

        * Algekule / Moseball
        * Skapt av to karer med bakgrunn fra Google Brain og Palantir
        * Ønsker å finne opp notebook-hjulet på nytt og erstatte bl.a
            * jupyter
            * streamlit
            * jupytext
            * ipywidgets
            * papermill
        """
    ).left()
    mo.hstack(
        [
            text,
            img,
        ]
    )
    return img, text


@app.cell
def _(mo):
    mo.image("./assets/star-history.png", width=800, height=500)
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md("# Hva gjør Marimo anderledes?"),
        mo.accordion({"Maintainability": "For jupyter stemmer ikke nødvendigvis koden med output eller program state. Hvis celler slettes så holdes variabler i minnet. Brukere kan kjøre celler i valgfri rekkefølge. Marimo Garanterer at kode, output og program-state er konsistent",
                      "Reactivity": "Når en celle kjøres, kjøres alle avhengige celler. Rekkefølge av cellene er ikke viktig",
                      "Interactivity": "Marimo inneholder mange innebygde UI-elementer som er synkronisert med python. ",
                      "Reuseability": "Lagret som python filer (`.py`). Kan kjøres som python script",
                      "Shareability": "Notebooks kan enkelt deles som en interaktiv web-app eller slides",
                      "Git-vennlig": "Notebooks lagres som `.py`-filer. Mindre diffs, mindre json-bloat"
                      })
    ])
    return


@app.cell
def _(mo):
    mo.md(
        """
        # Hvordan kjøres Marimo notebooks?
        * References / `refs`: Globale variable cellen leser men ikke definerer selv
        * Definitions / `defs`: Globale variabler cellen definerer
        * `refs` og `defs` lager en DAG som bestemmer rekkefølge på celle-eksekvering
        """
    )
    return


@app.cell
def _(mo):
    mo.vstack([mo.md(" # Betydelige endringer Marimo og Jupyter"), mo.accordion({
        "Celle-eksekvering": "Når en celle kjøres i Marimo, kjøres alle avhengige celler automatisk. Tilpasninger kan gjøres for å ikke automatisk eksekvere 'dyre' celler",
        "Redefinere variabler": """
        Variabler kan ikke redefineres i ulike celler. Dette er på grunn av hvordan `refs` og `defs` definerer DAG'en.
        Kan komme rundt det ved å f.eks: Innkapsle i funksjoner for å begrense globale variabler. Lage lokale, temporary variabler med underscore. Mutere variabler i cellene som definerer dem
        """,
        "Ingen magic/console commands": "Man kan ikke bruke f.eks `%%timeit` eller installere pip-pakker direkte i celler. Finnes workarounds",
        "`.py` vs `.ipynb`": "Metadata og outputs lagres ikke",
    })])
    return


@app.cell
def _(mo):
    mo.md(
        """
        # Demo

        * [Widgets / UI elementer](https://marimo.app/?slug=ia3872)
        * [Plotting](https://marimo.app/?slug=lxp1jk#)
        * [Layout](https://marimo.app/?slug=14ovyr)
        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
