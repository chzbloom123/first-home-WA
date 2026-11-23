# Your First Home in Washington

A free, plain-language overview of buying a first home in Washington State, with a local section for the Tri-Cities (Richland, Kennewick, Pasco, West Richland).

No sign-up, no ads, no tracking. The home page is the whole process in eight steps and takes about ten minutes to read. The other sections go deeper.

**This is education, not legal, lending, tax or insurance advice.** It is an independent guide, not a government site. It was built with AI assistance from official sources gathered in November 2026. Last reviewed: November 23, 2026.

## What is in this repository

| File | What it is |
|---|---|
| `index.html` | The finished site. One file. This is the only file a web host needs. |
| `src/content_home.py` | The words for the home page (the eight steps). |
| `src/content_a.py` | The words for Money, Loans, and Help and classes. |
| `src/content_b.py` | The words for Home types, Contract and closing, and Inspections. |
| `src/content_c.py` | The words for First year, Tri-Cities, the checklist, About, and the list of glossary terms shown. |
| `src/glossary.json` | One-sentence definitions for the glossary. |
| `src/source_links.txt` | Every official link collected during research. The build refuses to pass a link that is not on this list. |
| `src/build.py` | The script that turns the files above into `index.html` and runs the checks. |

## Putting it online

`index.html` sits at the top of the repository, so a static host (Vercel, Netlify, GitHub Pages) can serve it with no build step and no settings.

## Changing the words

1. Edit the text in one of the `src/content_*.py` files. The text is written in Markdown.
2. Rebuild:

   ```
   pip install markdown
   python3 src/build.py
   ```

3. Read what the build prints:
   - `not in source list: []` means every outside link is one that was collected during research. If a link shows up in that list, it was typed in by hand and needs checking before it is added to `src/source_links.txt`.
   - The word count and reading grade for each section. The home page target is about 1,800 words at or under an 8th grade level.
4. Commit `index.html` together with the file you edited.

## Keeping it true

Rules and numbers change. Review the site at least once a year, and sooner for these:

| When | What to re-check |
|---|---|
| Late 2026 | New loan limits for 2027 (the site links to the official lookups instead of printing the numbers) |
| January 1, 2027 | New version of the Washington seller disclosure form |
| January 1, 2027 | FHA's change to how it picks the credit score it uses |
| February 1, 2027 | Septic inspection required when a property changes hands |
| Any time | Tri-Cities down payment program funding status, city by city |
| January 1, 2028 | Washington's older condo and HOA laws are replaced |

When you finish a review, update the "Last reviewed" date in `src/build.py` (the `REVIEWED` line) and on the About page text in `src/content_c.py`, then rebuild.

## What the site will not do

- Recommend any lender, broker, inspector, insurer or contractor.
- Print "typical" Washington figures that no official source publishes, such as typical earnest money or the usual number of days for a contract deadline. It says "set in your contract" instead.
