"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    # Lectura de datos
    df = pd.read_csv('./files/input/news.csv', index_col=0)
    
    # Parámetros estéticos
    colors = {
        'Television': 'dimgray',
        'Newspaper': 'gray',
        'Radio': 'lightgray',
        'Internet': 'tab:blue'
    }
    
    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Radio': 2,
        'Internet': 3
    }

    zorders = {
        'Television': 1,
        'Newspaper': 1,
        'Radio': 1,
        'Internet': 2
    }

    # Inicializar gráfico
    plt.Figure()

    for col in df.columns:
        # Gráfico de lineas
        plt.plot(
            df[col],
            color=colors[col],
            label=col,
            linewidth=linewidths[col],
            zorder=zorders[col]
        )

        # Resaltar valores del primer año
        first_year = df.index[0]
        plt.scatter(
            first_year,
            df[col][first_year],
            color=colors[col]
        )

        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + ' ' + str(df[col][first_year]) + '%',
            ha='right',
            va='center',
            color=colors[col]
        )

        # Resaltar valores del último año
        last_year = df.index[-1]
        plt.scatter(
            last_year,
            df[col][last_year],
            color=colors[col]
        )

        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + '%',
            ha='left',
            va='center',
            color=colors[col]
        )
    
    plt.xticks(df.index, df.index)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.suptitle('How people get their news', fontsize=16)
    plt.title(
        'An increasing proportion cite the internet as their primary news source',
        fontsize=8
    )

    # Guardar gráfico
    if not os.path.exists('./files/plots'):
        os.makedirs('./files/plots')
    plt.tight_layout()
    plt.savefig('./files/plots/news.png')

    plt.show()
pregunta_01()