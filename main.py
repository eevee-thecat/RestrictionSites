import re


def main():
    dna_seq = input("Enter a DNA sequence: ")
    restriction_site = input(
        "What is the cut site sequence of the restriction enzyme? "
    )
    replacement_index = len(restriction_site) // 2
    replacement_string = (
        restriction_site[:replacement_index]
        + " | "
        + restriction_site[replacement_index:]
    )
    regex = re.compile(restriction_site)
    matches = list(regex.finditer(dna_seq))

    if len(matches) == 0:
        print("Error: could not find cut site in provided DNA sequence")
        exit(1)

    print(f"Cut sites found: {len(matches)}")
    new_seq = regex.sub(replacement_string, dna_seq)
    print("DNA sequence after cuts: ", new_seq)


if __name__ == "__main__":
    main()
