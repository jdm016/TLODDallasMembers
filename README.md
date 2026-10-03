# TLOD Dallas Member Portal

Member portal for Top Ladies of Distinction, Inc., Dallas Chapter: chapter calendar, programs and projects tracker, leadership and committees, resources, and feedback.

The site is plain HTML with one data file. There is no build step.

```
site/
  index.html          the portal page
  data/portal.json    everything the page shows (events, projects, committees, resources)
  robots.txt          keeps search engines out
docs/
  operations-manual.md   repository copy of the Chapter Operations Manual
  committee-success-kit.md   Committee Chair and Co-Chair Success Kit, 2026-2027
netlify.toml          Netlify settings (publish the site/ folder)
tools/build_artifact.py   builds the single-file Claude artifact version
```

## Connect to Netlify

1. Sign in at [app.netlify.com](https://app.netlify.com).
2. Choose **Add new site**, then **Import an existing project**, then **GitHub**.
3. Pick `jdm016/TLODDallasMembers`.
4. Netlify reads `netlify.toml`, so leave the build command empty and the publish directory as `site`.
5. Select **Deploy**. Every change pushed to the production branch republishes the site within a minute.
6. Optional: under **Domain management**, rename the site (for example `tloddallas.netlify.app`) or add a chapter domain.

### Keeping the site private

A Netlify site is public to anyone who has the link. The page asks search engines not to list it, and the directory, roster, and forms it links to stay protected by their Google sharing settings. To require a password for the whole site, turn on **Site configuration > Access & security > Password protection** (a Netlify Pro feature).

Do not add addresses, phone numbers, birthdays, account numbers, photo album invite links, or any teen information to `portal.json`.

## Updating the portal

Edit `site/data/portal.json` on GitHub (open the file, select the pencil icon, make the change, then **Commit changes**). Netlify republishes automatically.

| To change | Edit this list | Fields |
| --- | --- | --- |
| Calendar | `events` | `title`, `date` (YYYY-MM-DD), `start` and `end` (24-hour, like `18:30`), `location`, `type`, `contact`, `details` |
| Programs and projects | `projects` | `name`, `committee`, `lead`, `status` (Idea, Planning, In progress, Complete, On hold), `start`, `due`, `progress` (0 to 100), `notes`, `confirm` |
| Leadership and committees | `committees` | `group`, `name`, `chair`, `cochair`, `charge` |
| Resources | `resources` | `group`, `title`, `url`, `note` |
| Announcements | `announcements` | `title`, `date`, `author`, `body` |
| Feedback log | `heard` | `heard`, `status` (Received, Reviewing, Addressed), `date`, `response` |
| Feedback form link | `settings.feedbackFormUrl` | any https link |
| Bylaws quick reference | `bylaws` | `documentUrl` (link to the full bylaws), `sections` with `topic`, `reference` (article and section), `source` (Bylaws, Chapter records, or Add from the bylaws), `summary` |

Event types: Chapter, Executive Board, Committee, Program, Top Teens, Training, Deadline, Area / National, Social.

Give each new item a unique `id` (for example `e34`, `p14`). Keep commas between items; GitHub shows an error if the file stops being valid JSON.

## Operations Manual

`docs/operations-manual.md` is the repository copy. The living version, where Ladies comment and edit, is the Claude doc linked at the top of the file. When the doc changes, refresh this copy so both match.

## Claude artifact version

The same page also runs as a private Claude artifact where officers with edit access can update it in place. To refresh it from this repository:

```
python3 tools/build_artifact.py > build/portal-artifact.html
```

Then publish `build/portal-artifact.html` to the existing artifact.
