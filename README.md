# noetic-searx-scraper

This is a python script for scraping search results from the json api of [a public searx instance](https://github.com/asciimoo/searx/wiki/Searx-instances)\*. It was set up to scrape results for pages from [ipfs](https://ipfs.io), but the query can be changed to anything. The code isn't very pretty; you have to hardcode the number of pages of results you want to scrape. I'm sure there are lots of things that could be cleaned up with a little bit of work.

\* Ideally, you should just [run searx locally](https://github.com/asciimoo/searx#alternative-recommended-installation) and scrape that, so you don't put too much of a load on a public instance. I had troubles setting it up locally, but ymmv. If you do use a public instance, be mindful of how many pages you're scraping.

## Contributing

This whole thing could probably be made much nicer. I'm happy to accept any pull requests, although it's unlikely I'll work on it much myself.

## License

MIT.

