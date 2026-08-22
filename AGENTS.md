# AGENTS.md

## What this is

Not a code repo (no git, no build/test tooling). A collection of 32 PDF scans of
ACM A.M. Turing Award lectures plus a Chinese translation project.

- ALL 32 lectures are now translated. Original PDFs live in `translated/` named
  `<year>-<author>-<English Title>.pdf`; translations in `zh/<year>-<author>-<中文标题>.md`.
  The file index below maps original ACM DL DOI filenames to current locations.
- `README.md` is the human-facing bilingual index; keep it in sync with any file moves or corrections.

## Working with the PDFs

- `pdftotext` (Homebrew poppler) is installed and works: `pdftotext -l 1 <file>.pdf -` for a quick first page.
- Text quality varies wildly. Post-1985 issues extract cleanly; 1960s–70s scans have heavy OCR garbling
  (e.g. "Turning Lecture", mangled author names). Don't trust extracted text for exact quotes from older files —
  verify against the page image (`read` / `look_at`) if precision matters.
- PDF metadata (title/author fields) is useless — mostly null or temp-file names.

## Chinese translations (`zh/`)

Completed project: all 32 lectures translated into Chinese, one Markdown file per lecture,
named `zh/<year>-<author>-<中文标题>.md`.

Workflow that was used (validated on the Thompson pilot; keep for corrections/re-translations):
1. `pdftotext <file>.pdf -` for full prose — post-1980 prose extracts well even when titles/code are garbled.
2. Code figures and math are ALWAYS OCR-mangled (escapes like `\n` come out as `kn`, `\\` as `\V`).
   Render page images (`pdftoppm -png -r 150 <file>.pdf /tmp/out/page`) and `read` them to reconstruct code exactly.
3. Output format: translated prose + fenced code blocks + a final 译注 section for footnotes,
   OCR corrections, and translator additions (mark them as such). Reader asked for cultural
   annotations: gloss English adages, people, and period events (e.g. who Bobrow was, the 414s,
   "dance with the one that brought you") — use inline 〔译注N〕 markers, group notes by kind.
4. Known misprint: in 1283920.1283940 (Thompson), the printed captions for Figures 2.1 and 2.2
   are transposed on p. 762; translation follows the text logic, noted in 译注.

Copyright: ACM owns these; translations are for personal study only — do not publish.
NOTE (git): the repo at github.com:c2j/ACM-Turing-Award-Lectures ships ONLY zh/ + docs.
`translated/` (the PDFs) is gitignored and kept local-only for copyright reasons; README's
原文 column links to ACM DL DOIs instead. History was rebuilt to purge PDFs — never re-add them.

## Turing source papers (`papers/` → `papers-cn/`)

- `papers/` holds 6 PDFs: two standalone papers (Church 1936, "An Unsolvable Problem of
  Elementary Number Theory"; Sterrett, "Turing and the Integration of Human and Machine
  Intelligence", Feb 2012 Turing100 draft) and the four-volume North-Holland/Elsevier
  *Collected Works of A.M. Turing* (Mechanical Intelligence, Pure Mathematics, Morphogenesis,
  Mathematical Logic — ~1,000 pp total; Mechanical Intelligence & Pure Mathematics are
  image-only scans with NO text layer).
- The two standalone papers are translated into `papers-cn/` (same format as `zh/`, named
  `<year>-<author>-<中文标题>.md`). The four volumes are NOT translated — too large, two lack
  text layers; only their TOCs were inspected.
- NOTE: the current default model cannot read images (`read_image` fails), so math-heavy
  translations must reconstruct formulas from pdftotext output + domain knowledge and flag
  uncertain restorations in 译注 (this applied to the Church 1936 translation).

## File index (filename → lecture)

| File | Year | Author(s) | Lecture |
|---|---|---|---|
| 1283920.1283921 → translated/1966-perlis-The Synthesis of Algorithmic Systems.pdf | 1966 | Alan Perlis | The Synthesis of Algorithmic Systems |
| 1283920.1283922 → translated/1967-wilkes-Computers Then and Now.pdf | 1967 | Maurice Wilkes | Computers Then and Now |
| 1283920.1283923 → translated/1968-hamming-One Mans View of Computer Science.pdf | 1968 | Richard Hamming | One Man's View of Computer Science |
| 1283920.1283924 → translated/1969-minsky-Form and Content in Computer Science.pdf | 1969 | Marvin Minsky | Form and Content in Computer Science |
| 1283920.1283925 → translated/1970-wilkinson-Some Comments from a Numerical Analyst.pdf | 1970 | J. H. Wilkinson | Some Comments from a Numerical Analyst |
| 1283920.1283926 → translated/1971-mccarthy-Generality in Artificial Intelligence.pdf | 1971 | John McCarthy | Generality in Artificial Intelligence |
| 1283920.1283928 → translated/1973-bachman-The Programmer as Navigator.pdf | 1973 | Charles Bachman | The Programmer as Navigator |
| 1283920.1283929 → translated/1974-knuth-Computer Programming as an Art.pdf | 1974 | Donald Knuth | Computer Programming as an Art |
| 1283920.1283930 → translated/1975-newell-simon-Computer Science as Empirical Inquiry.pdf | 1975 | Newell & Simon | Computer Science as Empirical Inquiry |
| 1283920.1283931 → translated/1976-rabin-Complexity of Computations.pdf | 1976 | Michael Rabin | Complexity of Computations |
| 1283920.1283932 → translated/1976-scott-Logic and Programming Languages.pdf | 1976 | Dana Scott | Logic and Programming Languages |
| 1283920.1283933 → translated/1977-backus-Can Programming Be Liberated from the von Neumann Style.pdf | 1977 | John Backus | Can Programming Be Liberated from the von Neumann Style? |
| 1283920.1283934 → translated/1978-floyd-The Paradigms of Programming.pdf | 1978 | Robert Floyd | The Paradigms of Programming |
| 1283920.1283935 → translated/1979-iverson-Notation as a Tool of Thought.pdf | 1979 | Kenneth Iverson | Notation as a Tool of Thought |
| 1283920.1283936 → translated/1980-hoare-The Emperors Old Clothes.pdf | 1980 | C.A.R. Hoare | The Emperor's Old Clothes |
| 1283920.1283937 → translated/1981-codd-Relational Database A Practical Foundation for Productivity.pdf | 1981 | Edgar Codd | Relational Database: A Practical Foundation for Productivity |
| 1283920.1283938 → translated/1982-cook-An Overview of Computational Complexity.pdf | 1982 | Stephen Cook | An Overview of Computational Complexity |
| 1283920.1283939 → translated/1983-ritchie-Reflections on Software Research.pdf | 1983 | Dennis Ritchie | Reflections on Software Research |
| 1283920.1283940 → translated/1983-thompson-Reflections on Trusting Trust.pdf | 1983 | Ken Thompson | Reflections on Trusting Trust |
| 1283920.1283941 → translated/1984-wirth-From Programming Language Design to Computer Construction.pdf | 1984 | Niklaus Wirth | From Programming Language Design to Computer Construction |
| 1283920.1283942 → translated/1985-karp-Combinatorics Complexity and Randomness.pdf | 1985 | Richard Karp | Combinatorics, Complexity, and Randomness |
| 1283920.1283943 → translated/1986-hopcroft-Computer Science The Emergence of a Discipline.pdf | 1986 | John Hopcroft | Computer Science: The Emergence of a Discipline |
| 1283920.1283944 → translated/1986-tarjan-Algorithm Design.pdf | 1986 | Robert Tarjan | Algorithm Design |
| 1283920.1283945 → translated/1987-cocke-The Search for Performance in Scientific Processors.pdf | 1987 | John Cocke | The Search for Performance in Scientific Processors |
| 1283920.1283946 → translated/1988-sutherland-Micropipelines.pdf | 1988 | Ivan Sutherland | Micropipelines |
| 1283920.1283947 → translated/1990-corbato-On Building Systems That Will Fail.pdf | 1990 | Fernando Corbató | On Building Systems That Will Fail |
| 1283920.1283948 → translated/1991-milner-Elements of Interaction.pdf | 1991 | Robin Milner | Elements of Interaction |
| 1283920.2159562 → translated/1992-lampson-Principles for Computer System Design.pdf | 1992 | Butler Lampson | Principles for Computer System Design |
| 1283920.1283951 → translated/1994-feigenbaum-How the What Becomes the How.pdf | 1994 | Edward Feigenbaum | How the "What" Becomes the "How" |
| 1283920.1283952 → translated/1994-reddy-To Dream the Possible Dream.pdf | 1994 | Raj Reddy | To Dream the Possible Dream |
| 259380.259407 → translated/1996-pnueli-Verification Engineering A Future Profession.pdf | 1996 | Amir Pnueli | Verification Engineering: A Future Profession (abstract only, 1 page) |
| 1283920.2159561 → translated/1998-gray-What Next A Dozen Information-Technology Research Goals.pdf | 1998 | Jim Gray | What Next? A Dozen Information-Technology Research Goals (MS-TR-99-50) |

Note: 1283920.1283927 (Dijkstra 1972, The Humble Programmer) is absent from the collection.

## Acquired originals (now translated, moved to translated/)

- `translated/1972-dijkstra-The Humble Programmer (EWD340).pdf` — UT Austin EWD archive authorized
  reproduction. NOTE: image-only PDF, NO text layer (pdftotext yields nothing) — work from page images.
- `translated/1993-stearns-Its Time to Reconsider Time (author preprint).pdf` — author's homepage via
  web.archive.org; Type-3 bitmap fonts, pdftotext output is garbage, work from page images.
- `translated/2021-dongarra-The Evolution of Mathematical Software.pdf` — netlib author copy of CACM 65(12) 2022 (digital-born, clean).
- Their translations: `zh/1972-dijkstra-谦卑的程序员.md`, `zh/1993-stearns-是时候重新考虑时间了.md`, `zh/2021-dongarra-数学软件的演进.md`.
- 7 more CACM Turing lecture papers downloaded by the user from ACM DL (all now in translated/ with zh/ translations):
  Hartmanis 1993 (1283920.1283949, scanned), Naur 2005 (1188913.1188922), Clarke/Emerson/Sifakis 2007
  (1592761.1592781), Stonebraker 2014 (2869958), Hennessy/Patterson 2017 (3282307),
  Bengio/Hinton/LeCun 2018 (3448250), Aho/Ullman 2020 (3490685). All digital-born except Hartmanis.
- Hartmanis 1993 (CACM 37(10), DL id 1283920.1283949) exists in the open ACM backfile but dl.acm.org
  returns 403 to curl/scripts — download needs a real browser.
- Never published as papers (video only): 1989 Kahan, 1995 Blum, 1997 Engelbart, 1999+ most years;
  written CACM Turing papers exist for 2005 Naur, 2007 Clarke/Emerson/Sifakis, 2014 Stonebraker,
  2017 Hennessy/Patterson, 2018 Bengio/Hinton/LeCun, 2020 Aho/Ullman. Full table in README.md.
