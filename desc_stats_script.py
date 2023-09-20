from lib import descriptive_statistics, load_baseball_data, visualize_baseball_data

def load_describe_and_visualize_baseball_data(print_desc=False) -> None:
    # Load baseball data
    baseball_df = load_baseball_data()
    # Describe baseball data and save to csv
    desc_df = descriptive_statistics(baseball_df)
    if print:
       print(desc_df)
    desc_df.to_csv('descriptive_statistics.csv')
    # Visualize baseball data
    visualize_baseball_data(baseball_df)

if __name__ == "__main__":
    load_describe_and_visualize_baseball_data(print_desc=True)
  