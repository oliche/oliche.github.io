from pathlib import Path
import random

# gets the header from the current file
with open(Path().absolute().joinpath("2022-12-19-citations_sample.md")) as fp:
	quotes = fp.read()
quotes = quotes.split('---')
header = quotes[1]

with open(Path().absolute().joinpath("2022-12-18-citations.md")) as fp:
	quotes = fp.read()


# gets all quotes
quotes =  quotes.split('---')
header = quotes[1]
quotes = quotes[2]
quotes = quotes.split('**\n')


# selects randomly eight of them
quotes = random.sample(quotes, 8)
with open(Path().absolute().joinpath("2022-12-20-citations_sample.md"), 'w+') as fp:
	fp.write('---' + header + '---')
	for q in quotes:
		fp.write(q + '**\n')
