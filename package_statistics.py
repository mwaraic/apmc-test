from core.contents import Contents
import sys


def run(architecture: str):
    """
    Run statistics workload
    """
    obj = Contents(architecture=architecture)  # initialize Contents obj

    try:
        file = obj.download()  # download file
    except Exception:
        print('architecture not found')  # console error
        sys.exit()  # exit

    data = obj.parse(file)  # parse file

    df = obj.transform(data)  # transform table

    print(obj.statistics(df))  # console statistics


if __name__ == "__main__":

    args = sys.argv  # retrieve CLI args

    run(architecture=args[1])  # run workload
