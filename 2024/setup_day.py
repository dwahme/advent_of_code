
import argparse
import os
import pathlib
import shutil

def set_up_file_if_not_exists(path, file, source=None):
    filepath = os.path.join(path, file)

    if os.path.isfile(filepath):
        print(f"Base file {filepath} already exists, skipping")
    else:
        if source is not None:
            sourcepath = os.path.join(path, source)
            print(f"Generating file {filepath}, copied from {sourcepath}")
            shutil.copy(sourcepath, filepath)
        else:
            print(f"Generating file {filepath}, creating blank file")
            open(filepath, "a").close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set up day N for Advent of Code")
    parser.add_argument("day", action="store", type=int, help="The day of Advent of Code to set up")
    parser.add_argument("-s", action="store", dest="samples", type=int, help="The number of sample input files to set up", default=0)

    args = parser.parse_args()

    path = pathlib.Path(__file__).parent.resolve()
    day_str = f"{args.day:02}"

    print(f"Setting up day {args.day} in path context {path}...")
    print()

    python_filename = f"day{day_str}.py"
    set_up_file_if_not_exists(path, python_filename, "template.py")

    print()
    print(f"Setting up input files for {args.inputs} input")
    input_file = os.path.join("inputs", f"{day_str}.in")
    set_up_file_if_not_exists(path, input_file)

    if args.samples:
        print()
        print(f"Setting up sample input files for {args.samples} samples")

        if args.samples == 1:
            sample_file = os.path.join("inputs", f"sample-{day_str}.in")
            set_up_file_if_not_exists(path, sample_file)
        else:
            for i in range(1, args.samples + 1):
                sample_file = os.path.join("inputs", f"sample-{day_str}-{i:02}.in")
                set_up_file_if_not_exists(path, sample_file)
