import sys
from collections import Counter

def read_fasta(file):
    sequences = []
    seq = ""

    with open(file) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if seq:
                    sequences.append(seq)
                    seq = ""
            else:
                seq += line
        if seq:
            sequences.append(seq)

    return sequences

def count_kmers(sequences, k):
    counts = Counter()
    for seq in sequences:
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            counts[kmer] += 1
    return counts

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python kmer_counter.py <fasta_file> <k>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    k = int(sys.argv[2])

    sequences = read_fasta(fasta_file)
    counts = count_kmers(sequences, k)

    with open("results/kmer_counts.txt", "w") as out:
        for kmer, count in counts.items():
            out.write(f"{kmer}\t{count}\n")

    print(f"K-mer analysis finished for k={k}. Results saved in results/kmer_counts.txt")
