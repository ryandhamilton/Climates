# Getting climateshq.com live, step by step

Do these in order. Parts 1 and 2 happen on github.com, Part 3 on godaddy.com, Part 4 is waiting, Part 5 is how you edit the site afterward.

## Part 1: put the site on the main branch (5 clicks)

1. Go to https://github.com/ryandhamilton/Climates
2. You'll likely see a yellow banner saying `claude/climates-website-ndp5so had recent pushes` with a green button: **Compare & pull request**. Click it. (No banner? Click the **Pull requests** tab, then **New pull request**, set "compare" to `claude/climates-website-ndp5so`, and click **Create pull request**.)
3. Click the green **Create pull request** button.
4. Click the green **Merge pull request** button, then **Confirm merge**.
5. Done. The website files are now on the `main` branch.

## Part 2: turn on GitHub Pages (the free hosting)

1. Still in the repo, click **Settings** (top of the page, gear icon).
2. In the left sidebar, click **Pages**.
3. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: **main**, folder: **/ (root)**
   - Click **Save**.
4. In the **Custom domain** box on the same page, type `climateshq.com` and click **Save**.
5. GitHub will show "DNS check unsuccessful" in red. That's expected. It stays red until Part 3 is done.

## Part 3: point GoDaddy at GitHub

1. Log in at godaddy.com. Click your name (top right), then **My Products**.
2. Find **climateshq.com**, click the three dots or **DNS** next to it (may be labeled "Manage DNS").
3. You're now on a page listing DNS records. First, clean up:
   - If there's an **A** record with Name `@` (it usually points to "Parked" or a number like 34.x.x.x), click its pencil/trash icon and **delete it**.
   - If there's a **CNAME** record with Name `www`, delete that too.
   - If a "Forwarding" section at the bottom of the page has anything in it, delete/turn that off.
4. Now add 4 new records. For each: click **Add New Record**, choose Type **A**, Name `@`, TTL default is fine, and use these values (one record per line):
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
5. Add 1 more record: Type **CNAME**, Name `www`, Value `ryandhamilton.github.io`
6. Save. You're done with GoDaddy.

## Part 4: wait, then flip on HTTPS

1. Wait 15 to 60 minutes (DNS takes time to spread).
2. Go back to the repo → **Settings** → **Pages**. When the DNS check shows a green tick, tick the **Enforce HTTPS** checkbox. (If the checkbox is grayed out, wait another 15 minutes; GitHub is issuing your free certificate.)
3. Open https://climateshq.com. That's it, you're live. www.climateshq.com works too.

If something looks wrong after an hour: on the Pages settings screen, remove the custom domain, save, re-add it, save. That re-runs the check. And https://www.whatsmydns.net/#A/climateshq.com shows whether the world sees your new A records yet.

## Part 5: how to edit the site from now on

Every change you save to the `main` branch republishes the site automatically in about a minute. No deploy button, no FTP.

### The no-tools way (edit in the browser)

1. Go to https://github.com/ryandhamilton/Climates and click the file you want (almost everything you'd change is in `index.html`).
2. Click the **pencil icon** (top right of the file view).
3. Make your edit, then click the green **Commit changes** button. Choose "Commit directly to the main branch". Wait a minute, refresh climateshq.com.

Where things live in `index.html`:
- Headlines and body text: search the file for the sentence you want to change and retype it.
- **Newsletter posts**: find `class="posts"`. Each post is one `<a class="post reveal" ...>` block: a link, a date, a title, a one-line dek. Copy an existing block, paste it at the top of the list, and swap in the new edition's URL, date, title, and subtitle. Delete the bottom one if the list gets long.
- **Images**: files live in `assets/img/`. To swap one, upload a new file there (repo → `assets/img` → **Add file** → **Upload files**) and either reuse the same filename or update the filename referenced in `index.html` (cards, about) or `css/style.css` (hero is in `index.html`; the two full-width photo bands are in `style.css`, search for `band-mates` and `band-solar`).
- Colors and fonts: top of `css/style.css`, the `:root` block.

### The zero-effort way

Open a Claude session on this repo and say what you want ("swap the hero image for something with a coastline", "add the new edition to the posts list", "change the contact email"). It edits, you review, it pushes.

### If you ever break something

Repo → **Commits** (clock icon on the main page) shows every version. Open the last good one to see the old text, or ask Claude to revert.
