# Climates

Climates is an advisory practice and communications agency working to make climate change a more accessible and engaging topic for general audiences.

## The website

A static one-page site, no build step.

- `index.html` — all content: services, why Climates, the newsletter, about, contact
- `css/style.css` — styles
- `js/main.js` — mobile nav and footer year
- `favicon.svg` — favicon

To preview locally, open `index.html` in a browser, or run:

```bash
python3 -m http.server 8000
```

and visit http://localhost:8000.

To deploy on GitHub Pages: Settings → Pages → deploy from branch, root folder. No other setup needed.

Newsletter posts in the writing section are hardcoded from the [Substack feed](https://climatesnewsletter.substack.com/feed); refresh them when there's a new edition worth featuring.
