# Coding Test

## Command

`make start`

## Approach and Thought Process

- Identified from instructions that functionalities of the tool are architecture (input), download, parse and statistics (output)

- Read documentation and evaluated schema of the table

- Downloaded gzip file, decompressed it and viewed indices

- Created a notebook and installed required packages

- Allocated sample data for testing so its easier to validate results

- Wrote parse function

- Further evaluated schema of the table to find that column qualified packages names need to be transformed

  * Splitting by `,` and exploding to get one to one mapping of package with filename

  * Splitting by `/` to get package name since its formatted as section/name

- Wrote transform function

- Wrote statistics function

- Found that the string `Contents-{architecture}.gz` extends the url of mirror so extracting hrefs through web scrapping is not required

- Looked into gzip function for decompression

- Wrote download function

- Wrote Contents class, inserted all functions and tested end-to-end with different architectures

- Organized work from notebook into file dir structure

- Added tests and containerized the tool

## Completion Time

~ 4 hrs 15 mins