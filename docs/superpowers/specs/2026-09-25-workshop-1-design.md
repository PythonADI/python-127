# python-127 — Workshop 1 Design

## Context

`python-127` is a fresh beginner Python course, independent of the
`PythonADI/python-126` cohort (that course is used only as a structural
and content reference, not a prerequisite — python-127 students are not
assumed to have taken it).

Two repos informed this design:

- **`PythonADI/python-126`** — previous beginner Python course. Its
  layout (`docs/workshop_N.md` + `workshop_N/` + `docs/workshop_N_homework.md`
  + `presentations/Workshop N.html`) and its workshop 1 content (how
  computers work → programming → Python basics → variables/types/casting/
  operators) are the template for python-127's structure and workshop 1
  scope.
- **`JavaScriptADI/javascript-205`**, specifically the
  `javascript-205-homework-6` repo — the mature homework-submission
  pattern to replicate: a separate per-homework repo with
  `README.md`/`EXERCISES.md`/`SUBMITTING.md`, a `submissions/<username>/`
  folder convention, `.github/CODEOWNERS` auto-assigning the instructor
  as reviewer, and a `.github/pull_request_template.md` checklist.
  Students fork the homework repo, branch as `<github-username>`, commit
  their work into their own submissions folder, and open a PR titled
  `"Homework N - Your Name"`.

This spec covers only **workshop 1** (course infrastructure + first
workshop content + first homework repo), as the first sub-project of the
larger "design python-127" effort. Later workshops repeat this same
pattern and get their own lightweight follow-up (no separate spec
needed — the pattern is established here).

## Decisions

1. **Course scope**: python-127 is a fresh beginner course. Workshop 1
   mirrors python-126's workshop 1 territory (adapted, not copy-pasted).
2. **Homework mechanism**: PR-based from homework 1 onward (no phase-in
   period), adapted with much more explicit hand-holding than
   javascript-205's SUBMITTING.md, since these students have never used
   Git before (unlike javascript-205 students by homework 5, who'd
   already done homeworks 1-4).
3. **Homework repo location**: new repos under the `PythonADI` GitHub
   org (confirmed: `tavkhelidzeluka` has push access, matches the
   `CODEOWNERS` reviewer identity used in javascript-205).
4. **Language**: bilingual. Every homework doc (`README.md`,
   `EXERCISES.md`, `SUBMITTING.md`, `submissions/README.md`) gets an
   English version and a `_ka.md` Georgian version, matching
   javascript-205-homework-6 and python-126's Georgian-aware audience.

## Repo 1: `PythonADI/python-127` (course repo, this working directory)

Mirrors python-126's layout. No `.github/` or CONTRIBUTING here — PR
mechanics live entirely in the per-homework repo, matching how
javascript-205 keeps its main repo free of homework machinery from
homework 3 onward.

```
README.md                       — syllabus/index: links workshop 1's
                                   lesson + presentation + homework repo
docs/workshop_1.md               — lesson text (English; Georgian input()
                                   prompts inline where natural, matching
                                   python-126's convention — not a full
                                   docs/workshop_1_ka.md translation)
docs/resources.md                — reading list, carried over/adapted
                                   from python-126
presentations/Workshop 1.html    — self-contained static HTML slide deck
workshop_1/                      — small standalone example .py scripts
                                    (no loops/functions/collections —
                                    not taught yet)
```

## Repo 2: `PythonADI/python-127-homework-1`

```
README.md / README_ka.md               — what this homework covers, links
                                          to EXERCISES.md and SUBMITTING.md
EXERCISES.md / EXERCISES_ka.md          — the Python exercises + expected
                                          output, constrained to concepts
                                          taught in workshop 1
                                          (variables/types/casting/operators):
                                            1. About me (f-strings)
                                            2. Fix a TypeError bug (casting)
                                            3. Rectangle area/perimeter
                                            4. Odd/even via %
                                            5. Bonus: seconds in a day/week
SUBMITTING.md / SUBMITTING_ka.md        — full beginner walkthrough: install
                                          Git, create a GitHub account,
                                          configure user.name/email, fork
                                          this repo, clone your fork, create
                                          a branch named after your GitHub
                                          username, add your files under
                                          submissions/<username>/, commit,
                                          push, open a PR titled
                                          "Homework 1 - Your Name" against
                                          PythonADI/python-127-homework-1,
                                          respond to review feedback on the
                                          same branch (never open a second
                                          PR)
submissions/README.md / README_ka.md    — explains the one-folder-per-
                                          student convention with a worked
                                          example
.github/CODEOWNERS                      — "* @tavkhelidzeluka"
.github/pull_request_template.md        — checklist mirroring EXERCISES.md
                                          (files present, runs without
                                          errors, didn't touch other
                                          files/folders, GitHub username
                                          and folder path filled in)
```

No CI/test automation — review is manual via the CODEOWNERS-triggered
PR review, matching javascript-205 (no GitHub Actions anywhere in that
org).

## Out of scope for this spec

- Workshops 2+ and their homework repos (repeat this pattern once
  workshop 1 is built and reviewed).
- A course-wide top-level README tying all workshops together (only
  workshop 1's entry is needed for now).
- Any CI/autograding — explicitly not used by the reference courses.

## Testing / verification

This is instructional content, not application code — "testing" means:
- Every example script in `workshop_1/` runs cleanly with
  `python workshop_1/<file>.py` under Python 3.12+.
- Every exercise in `EXERCISES.md` has a working reference solution
  used to verify the stated expected output before publishing.
- `python-127-homework-1`'s fork → branch → PR flow is walked through
  once end-to-end (as a test account or dry run) before being handed to
  students, to confirm CODEOWNERS review-assignment and the PR template
  actually render as expected on GitHub.
