from core.contents import Contents
import sys


def run(architecture: str):
    """
    Run workload
    """
    obj = Contents(architecture=architecture)  # initialize Contents obj

    try:
        file = obj.download()
    except Exception:
        print('architecture not found')  # console error
        sys.exit()  # exit

    data = obj.parse(file)

    df = obj.transform(data)

    print(obj.statistics(df))  # console statistics


if __name__ == "__main__":

    args = sys.argv  # retrieve CLI args

    run(architecture=args[1])
