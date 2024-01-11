import matplotlib.pyplot as plt


def load_sequence_lengths():
    pass


def plot_sequence_lengths(sequence_lengths):
    # Plot a histogram of sequence lengths
    plt.hist(sequence_lengths, bins=20, color="blue", edgecolor="black")
    plt.xlabel("Sequence Length")
    plt.ylabel("Frequency")
    plt.title("Distribution of Sequence Lengths")
    plt.show()


# Example usage
if __name__ == "__main__":
    sequence_lengths = (
        load_sequence_lengths()
    )  # Replace with actual data loading function
    plot_sequence_lengths(sequence_lengths)
