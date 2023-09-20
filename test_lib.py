from lib import load_baseball_data, descriptive_statistics, visualize_baseball_data
import os

def test_load():
    df_test = load_baseball_data()
    assert df_test.shape == (1015, 7)

def test_description():
    df_test = load_baseball_data()
    desc_df = descriptive_statistics(df_test)
    assert desc_df.shape == (8, 3)

def test_visualize():
    df_test = load_baseball_data()
    visualize_baseball_data(df_test)
    assert os.path.exists('position_counts.png')
    assert os.path.exists('weight_vs_height.png')
