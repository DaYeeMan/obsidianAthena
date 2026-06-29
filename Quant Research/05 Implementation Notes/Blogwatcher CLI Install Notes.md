---
type: install-notes
tags: [quant-research, blogwatcher, rss, setup]
---

# Blogwatcher CLI Install Notes

`blogwatcher-cli` can provide persistent RSS/blog monitoring with read/unread state. During setup, Docker was available on this Windows machine, but Go was not found.

## Option A — Docker, recommended if you do not want native install

Use Docker with a persistent named volume:

```bash
docker run --rm -v blogwatcher-cli:/data -e BLOGWATCHER_DB=/data/blogwatcher-cli.db ghcr.io/julientant/blogwatcher-cli blogs
```

Scan feeds:

```bash
docker run --rm -v blogwatcher-cli:/data -e BLOGWATCHER_DB=/data/blogwatcher-cli.db ghcr.io/julientant/blogwatcher-cli scan
```

Add a feed/blog:

```bash
docker run --rm -v blogwatcher-cli:/data -e BLOGWATCHER_DB=/data/blogwatcher-cli.db ghcr.io/julientant/blogwatcher-cli add "Quantocracy" https://quantocracy.com --feed-url https://quantocracy.com/feed/
```

List unread articles:

```bash
docker run --rm -v blogwatcher-cli:/data -e BLOGWATCHER_DB=/data/blogwatcher-cli.db ghcr.io/julientant/blogwatcher-cli articles
```

This keeps state in the Docker volume named `blogwatcher-cli`.

## Option B — Go install, if Go is installed later

Install Go from https://go.dev/dl/ and make sure `go` is on PATH. Then run:

```bash
go install github.com/JulienTant/blogwatcher-cli/cmd/blogwatcher-cli@latest
```

Make sure Go's bin directory is on PATH. On Windows this is commonly:

```text
%USERPROFILE%\go\bin
```

In Git Bash, check:

```bash
command -v blogwatcher-cli
blogwatcher-cli --help
```

## Option C — Release binary

Check GitHub releases:

https://github.com/JulienTant/blogwatcher-cli/releases

If a Windows binary is available, download it, place it somewhere on PATH, and verify:

```bash
blogwatcher-cli --help
```

## Current Fallback

Until `blogwatcher-cli` is installed, the quant research system uses:

```text
Quant Research/_System/Scripts/feed_scan.py
```

That script is stdlib-only and was verified against Quantocracy, Alpha Architect, Robot Wealth, Quantpedia, and arXiv q-fin feeds. It does not maintain read/unread state like Blogwatcher does.
