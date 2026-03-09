# Sequence K-mer Analysis

This project implements a simple bioinformatics pipeline to **count k-mers in DNA sequences**.  
It is designed to be executed in a Linux environment and demonstrates basic bioinformatics workflow practices.

---

## Project goals

- Practice bioinformatics scripting using Python
- Learn how to automate analyses with Bash
- Use Git and GitHub for version control
- Build a small reusable pipeline for k-mer analysis

---

## Pipeline description

The pipeline performs the following steps:

1. Reads DNA sequences from a FASTA file
2. Counts all k-mers of a specified length (`k`)
3. Writes the counts to a results file (`results/kmer_counts.txt`)
4. Allows automation using a Bash script

---

## Project structure

```
sequence-kmer-analysis/
├── data/ # Input FASTA files
│ └── sample.fasta
├── scripts/ # Python and Bash scripts
│ ├── kmer_counter.py
│ └── run_kmers.sh
├── results/ # Output files
│ └── kmer_counts.txt
└── README.md
```
---

## Technologies used

- Python 3
- Bash
- Linux (Ubuntu / WSL)
- Git & GitHub

---

## How to run the pipeline

From the root directory of the project.

### Run using Python

```bash
python3 scripts/kmer_counter.py data/sample.fasta 3
```
data/sample.fasta → input FASTA file

3 → k-mer length

Results will be saved in:

results/kmer_counts.txt

### Run using the Bash script

Make the script executable (first time only):

```
chmod +x scripts/run_kmers.sh

```

Run the pipeline:

```
./scripts/run_kmers.sh data/sample.fasta 3

```

## Future improvements

- Add support for larger datasets

- Include sequence filtering steps

- Process multiple FASTA files

- Add visualization of k-mer frequencies

## Author

Paula
