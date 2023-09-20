from lib import descriptive_statistics, load_baseball_data, visualize_baseball_data


def load_describe_and_visualize_baseball_data() -> None:
    # Load baseball data
    baseball_df = load_baseball_data()

    # Describe baseball data
    desc_df = descriptive_statistics(baseball_df)
    print(desc_df)

    # Visualize baseball data
    visualize_baseball_data(baseball_df)

if __name__ == "__main__":
    load_describe_and_visualize_baseball_data()