from Bio import SeqIO


def read_sequence_file(file_path):
    # Read sequences from a file using Biopython
    sequences = list(SeqIO.parse(file_path, "fasta"))
    return sequences


def calculate_sequence_length(sequences):
    # Calculate the length of each sequence
    lengths = [len(seq) for seq in sequences]
    return lengths


# Example usage
if __name__ == "__main__":
    sequence_file_path = "data/sequences.fasta"  # Replace with actual file path
    sequences = read_sequence_file(sequence_file_path)
    sequence_lengths = calculate_sequence_length(sequences)
    print("Sequence Lengths:", sequence_lengths)
