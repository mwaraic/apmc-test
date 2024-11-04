import pandas as pd
import requests
import gzip


class Contents:

    BASE_URL = 'http://ftp.uk.debian.org/debian/dists/stable/main'

    def __init__(self, architecture: str):
        """
        Initialize Contents object
        """
        self.content = f'Contents-{architecture}.gz'

    def download(self) -> str:
        """
        Downloads compressed Contents file from a Debian mirror
        and decompresses it
        """
        response = requests.get(f'{self.BASE_URL}/{self.content}')  # download

        file = gzip.decompress(response.content)  # decompress

        return file.decode()  # deocde bytes -> string

    def parse(self, file: str) -> list:
        """
        Parses table from decompressed Contents file
        """
        # extract lines from file
        lines = [line.split(' ') for line in file.strip().split('\n')]

        data = []

        for line in lines:
            # a = filename, b = packages (qualified_packages_names)
            a, b = line[0], line[len(line) - 1]

            data.append({'filename': a, 'packages': b})

        return data

    def transform(self, data: list) -> pd.DataFrame:
        """
        Transforms packages (qualifed_package_names) column in table
        """
        # split packages col by , and explode
        df = pd.DataFrame(data) \
            .assign(package=lambda x: x['packages'].str.split(',')) \
            .explode('package')

        # split package col by / into seperate cols: section and package_name
        df[['section', 'package_name']] = df['package'].str \
                                                       .split('/', expand=True)

        # select package_name, filename
        return df[['package_name', 'filename']]

    def statistics(self, contents: pd.DataFrame) -> str:
        """
        Generate statistics from Contents DataFrame
        """
        # top 10 packages with most files associated with them
        return contents.groupby('package_name', as_index=False) \
                       .agg(number_of_files=pd.NamedAgg(column='filename',
                                                        aggfunc='count')) \
                       .sort_values('number_of_files', ascending=False)[:10] \
                       .to_string(index=False)
