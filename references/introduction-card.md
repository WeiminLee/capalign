# Introduction card

Domain-neutral. The inputs are booleans about the product in front of you.
The rule does not name a material, a code, a host, or a method family. Copy
`question`, `input`, `validity`, and `target` from this work and this host.
Do not reuse the wording of a previous card. A filled gold file, including
the mini fixture, is one instance of this function, not a template. A work
that never states a method does not get a card for that method.

The two projection gap tables stay separate. This card is a third object: one
solicit-able product, joined across the paper projection and the repo
projection. It is written before any host edit. This run does not apply the
card and does not execute its test.

## What opens a row

A row is one product a caller can ask for by itself. A package name, a
validity sentence, and a second name for the same product do not open rows.
Record them in `dropped`, or hang the validity sentence on `validity_slot`.

Fill slots from cited text. Do not fill `s` or `e` from a `confidence: low`
span. Each slot is an object:

```json
{"state": 1, "provenance": "paper", "span": "path:start-end", "quote": "verbatim"}
```

- `state: 1` — the source states it. Requires a non-empty verbatim `quote` and a
  `span`.
- `state: 0` — the source was inspected and does **not** state it. `span` names
  what was inspected (or is null only when that arm does not exist), `quote` may
  be empty, and `why_empty` says which case it is: `absent`, `no-paper-arm`,
  `no-repo-arm`.
- `state: "unknown"` — the source could **not** be inspected. `why_unknown` is
  required (`unreachable`, `not-consulted`, `unparsable`); `span` and `quote` are
  empty. **Unknown is not 0.** Never fill an unknown slot from the other arm —
  that is the contamination the blind inventory exists to prevent.
- `provenance` is fixed by the slot: `s` and `v_p` are `paper`; `e` and `v_r`
  are `repo`; `none` only when that arm does not exist. A value from the wrong
  arm is invalid, not merely low-confidence.

The paper arm's slots are frozen before the repo arm is read (blind dual
inventory, SKILL.md step 1). Record which method was used in
`surfaces.arms`; an unisolated run says so and caps paper-arm confidence at
`medium`.

| slot | 1 when |
|---|---|
| `s` | the paper states an ordered procedure for this product |
| `e` | the repo has a real entry (source or formal command). A doc that names a missing module is `e=0` |
| `v_p` | the paper states when the result is invalid |
| `v_r` | the repo states when the result is invalid |
| `kappa` | `s=e=1` and the two procedures are not the same computation. If that cannot be decided, `kappa=0`. `kappa=1` is forbidden unless `s=e=1`; `kappa` is meaningless unless both are 1 |

`host_has` is true only when the host already delivers this product. A nearer
skill or tool with a different product stays `nearest` and `host_has=false`.

## Label

Compute `lambda` from the slots. Do not override it.

| condition | `lambda` | `action` |
|---|---|---|
| `s=e=0` | `incongruent` | `ignore` (no card) |
| `s=1`, `e=0` | `obligation-sans-entry` | `install` |
| `s=0`, `e=1` | `entry-sans-obligation` | `refuse` |
| `s=e=kappa=1` | `procedure-conflict` | `refuse` |
| `s=e=1`, `kappa=0`, `v_p`,`v_r` known, `v_p!=v_r` | `validity-gap` | `install` |
| `s=e=1`, `kappa=0`, `v_p`,`v_r` known, `v_p==v_r` | `both-aligned` | `install` |
| `s` or `e` is `unknown` | `insufficient-evidence` | **no card**; the gap row is `unknown` |
| `s=e=1`, `kappa=0`, `v_p` or `v_r` is `unknown` | `validity-unassessed` | `install` with `prescribed: ["bind"]`; `validity` is `unknown (not assessed)` |

`insufficient-evidence` is the third outcome the four-question table needs: a
paper that was claimed but could not be read is **not** a paper that states
nothing. It produces no install card and no refuse card; the product stays in
the gap table as `unknown` and in Unresolved with `why_unknown`. Do not
substitute the repo arm's value for `s` to escape this state.

`validity-unassessed` may still install — the obligation and the entry are
established — but it must not claim a `check` primitive it could not derive. Its
card says the validity was not assessed, and Unresolved records why.

`boundary` is `in-question` when the host catalog already answers this
question, and `new-question` otherwise. A `new-question` card may still be
`install`. It is ranked last. Opening it is a human decision. It is not
alignment debt, and this run does not build it.

**`agent-competence` products get no card.** The host delivers them through the
agent plus a standard library, and the row already names the local check that
makes the result trustworthy. There is nothing to install; minting a card here is
how a code library's module list turns into a fake surface (`alignment-rules.md`
§Agent competence).

## Placement

Ask the placement questions (`alignment-rules.md` §Placement) only when
`action` is `install`. An install card has these fields and no others in
`placement`:

| field | required content |
|---|---|
| `target` | `extend:<host id>`, `new-skill:<id>`, `tool:<id>`, `script:<host skill id>`, or `runner` |
| `question` | the one question a caller would ask |
| `input` | the one input contract |
| `validity` | the invalidation clause a side actually stated. If both sides were inspected and neither stated one, the value is `none stated`; if a side could not be inspected, `unknown (not assessed)`. Do not invent one |
| `validity_owner` | `gate`, `runner`, or `skill-body` when a side stated an invalidation; otherwise null |
| `forbidden` | the one clause naming what not to do. It must show that no repo entry id is forged and the reference agent is not wrapped |

Cite the placement rule numbers in `rule`. Low-confidence evidence never
drives `install` (placement rule 5).

A second question, a second input contract, or a second invalidation regime
is a different card.

## Refusal

`action: refuse` is rule 7. `placement` is `null`. The card names no new
skill, tool, or extend target. Success is that the host is unchanged.

Use `refuse` for `entry-sans-obligation` and `procedure-conflict`. Do not
install a repo command the paper never obligates. Do not pick a side of a
procedure conflict.

## Test contract

The contract is text on the card. This run does not execute it.

| `action` | contract |
|---|---|
| `install` | `fail_before`, `pass_after`, and `destroy` are each one clause. `destroy` names which prescribed piece is removed: the entry binding, the paper procedure, or the invalidation check |
| `refuse` | `pass_after` states that the host is unchanged and that the product is absent from the paper's test set. `destroy` is `n/a` |

### The contract must exercise the bridge, not the docstring

An install card places a **bridge** (`alignment-rules.md` §What a skill is for):
the domain judgement the host agent does not already have. A contract that can be
satisfied by reading the prompt back tests instruction following, and a skill that
passes only that has not been shown to carry anything.

- **`fail_before` is the agent getting the task wrong without the skill** — not
  "the entry point does not exist". Missing entry points are what `destroy` is
  for; `fail_before` is about the agent's judgement.
- **`pass_after` is the agent getting it right because the body carried the
  missing judgement**, on a prompt that states the user's problem and nothing
  more. If the prompt names the skill, the entry point, and the required output
  in order, the case is testing the docstring.
- **Routing is part of the contract when the card is a skill or an extend.** For
  a skill card: a positive case (the user's own words select this skill) and a
  negative case (the neighbouring question it must not absorb). For an
  `extend:<host id>` card: a positive case (the existing skill still routes its
  original question) **and** a negative case (the neighbouring skill or question
  must not absorb the new one). Without both, an extend line is untested and
  fragmentation is invisible.

### Prescribed primitive (audit anchor)

So that a later patch can be audited statically (`π ∈ Adm(λ)`), every card
names the prescribed primitive set and the primitives it forbids. An empty
`prescribed` is legitimate (a refusal prescribes no host patch).

| `lambda` | `prescribed` | `forbidden_primitives` |
|---|---|---|
| `both-aligned` | `["bind"]` (add `"check"` when `v_p=v_r=1`) | `["impl"]` |
| `obligation-sans-entry` | `["impl"]` | `["bind"]` (a forged repo entry id is a violation, not a style) |
| `validity-gap` | `["bind", "check"]` | `[]` |
| `validity-unassessed` | `["bind"]` | `["impl", "check"]` (no validity was derived) |
| `entry-sans-obligation` | `[]` | `["bind", "impl"]` |
| `procedure-conflict` | `["record"]` (report-side only; no host patch) | `["bind", "impl"]` |
| `incongruent` / `insufficient-evidence` | `[]` (no card) | `["bind", "impl", "check"]` |

For an `install` card, `test.destroy` names **one** element of `prescribed`; after
removing it the test must fail again. For a `refuse` card, `destroy` is `n/a`
because there is no host patch to remove. A patch on a `refuse` card that contains
a forbidden primitive is invalid regardless of its text.

### Verification status

A written contract is not a passed test. Every card carries a `verification`
block so that any later report can state, per product, what was actually
executed:

| field | values |
|---|---|
| `beats.fail_before` | `pass` / `fail` / `not-run` — `pass` means the frozen host failed the test before the edit, as required |
| `beats.pass_after` | `pass` / `fail` / `not-run` |
| `beats.destroy` | `pass` / `fail` / `not-run` — `pass` means removing the prescribed primitive named by `test.destroy` turned the test red again; a beat that stays green is `fail` and voids the test |
| `evidence` | command + observed outcome per executed beat; empty when `not-run` |

Card status: `e2e-verified` (all applicable beats executed with the expected
outcome), `contract-only` (contract written, beats not run), or `failed`.
This skill's own run ends at the card, so its cards are `contract-only` by
construction — a report must never present a `contract-only` card's product
as delivered. For a `refuse` card, `e2e-verified` means the host was checked
unchanged and the product is absent from the paper test set; `destroy` stays
`n/a`.

A later build moves a card out of `contract-only` **only** by appending a build
record (`report-contract.md` §Build records): date, host commit, the three
commands and their observed outcomes. The alignment report is not edited in
place; the ledger points at the latest record. An `e2e-verified` claim whose
build record is missing is `contract-only`.

Priority orders `install` cards only: fix-wrongness (`validity-gap`, and a
`partial` gap on a question the host already answers), then honor-promise (a gap
the host's own audit already admits), then `new-question`.

The label table is closed (eight rows, two of which produce no card). A run that
happens to hit only two of them does not narrow the table.

## Projection tables

Do not copy a card back into either projection gap table, and do not merge
those two tables into one. `joins.paper` and `joins.repo` record which
projection ids this product absorbed.
