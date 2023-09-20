import pandas as pd
import matplotlib.pyplot as plt


def load_baseball_data() -> pd.DataFrame:
    df = pd.read_csv("https://raw.githubusercontent.com/datacamp/courses-introduction-to-python/master/datasets/baseball.csv")
    return df

def descriptive_statistics(df) -> pd.DataFrame:
    desc_df = df.describe()
    return desc_df

def visualize_baseball_data(df, plot_bar=True, plot_scatter=True) -> None:
    position_counts = df['Position'].value_counts()
    if plot_bar:
        fig, ax = plt.subplots()
        ax.bar(position_counts.index, position_counts)
        ax.set_xlabel('Position')
        ax.set_ylabel('Count')
        ax.set_title('Number of players in each position')
        ax.tick_params('x', labelsize=6)
        fig.savefig('position_counts.png')

    if plot_scatter:
        fig2, ax2 = plt.subplots()
        ax2.scatter(df['Height'], df['Weight'])
        ax2.set_xlabel('Height (inches)')
        ax2.set_ylabel('Weight (pounds)')
        ax2.set_title('Weight as a function of Height')
        fig2.savefig('weight_vs_height.png')