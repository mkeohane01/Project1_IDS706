from desc_stats_script import load_describe_and_visualize_baseball_data
import os

def test_load_describe_and_visualize_baseball_data():
    load_describe_and_visualize_baseball_data()
    assert os.path.exists('descriptive_statistics.csv')
    assert os.path.exists('position_counts.png')
    assert os.path.exists('weight_vs_height.png')