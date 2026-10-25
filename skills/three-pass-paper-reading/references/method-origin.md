# Method provenance and adaptations

Source: S. Keshav, *How to Read a Paper*, supplied two-page PDF. The visible footer identifies ACM SIGCOMM Computer Communication Review, volume 37, number 3, July 2007, printed pages 83–84. The original is available as a [University of Waterloo-hosted PDF](https://cs.uwaterloo.ca/~Brecht/courses/856/readings/how-to-read/keshav-paper-reading.pdf); the [author’s page](https://svr-sk818-web.cl.cam.ac.uk/keshav/publications/htrap.html) provides later versions and translations. The initial worked examples used a supplied copy of the 2007 version; its fingerprint is recorded in `examples/source-manifest.json` in the repository. This skill does not require that local file.

## Original method, paraphrased

| Source locator | Operational guidance retained |
|---|---|
| PDF p.1, §2 | Read in up to three passes, each with a distinct purpose, instead of immediately proceeding linearly through all details. |
| PDF p.1, §2.1 | First read title/abstract/introduction, headings, conclusion, and references; answer Category, Context, Correctness, Contributions, Clarity; decide whether further reading is worthwhile. Suggested human duration: 5–10 minutes. |
| PDF pp.1–2, §2.2 | Read more carefully while postponing detailed proofs, take notes, inspect figures/axes/error bars, mark unread references, and become able to explain the argument with evidence. If still confused, stop, return after background reading, or continue. Suggested human duration: up to one hour. |
| PDF p.2, §2.3 | Virtually recreate the work under the authors' assumptions, compare with the paper, challenge assumptions, examine presentation, note future ideas, and reconstruct the structure and strengths/weaknesses. Suggested human duration: 4–5 hours for beginners, about one hour for experienced readers. |
| PDF p.2, §3 | Begin a survey with 3–5 recent papers, use related work and shared citations to find surveys/key work, inspect active researchers and recent proceedings, make two passes through selected papers, and iterate. |
| PDF p.2, §4 | Adjust depth to need and available time; obtain the overall picture before getting lost in detail. |

## Added implementation practices

The source does not prescribe page-level evidence ledgers, PDF extraction/rendering tools, numerical consistency checks, machine-readable logs, or the exact report format. These are adaptations that make an agent's execution inspectable. The source asks for reconstructing the structure from memory; for an agent this is operationalized as writing an initial reconstruction, comparing against the source, and disclosing that this is not a human memory test.

Its graph/error-bar guidance motivates checking uncertainty; this skill does not treat the presence or absence of error bars alone as a significance test. Likewise, references/venues guide discovery but do not determine validity. A virtual reimplementation does not assert that code was run or experimental results were reproduced.
