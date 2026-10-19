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
span.

| slot | 1 when |
|---|---|
| `s` | the paper states an ordered procedure for this product |
| `e` | the repo has a real entry (source or formal command). A doc that names a missing module is `e=0` |
| `v_p` | the paper states when the result is invalid |
| `v_r` | the repo states when the result is invalid |
| `kappa` | `s=e=1` and the two procedures are not the same computation. If that cannot be decided, `kappa=0`. `kappa=1` is forbidden unless `s=e=1` |

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
| `s=e=1`, `kappa=0`, `v_p!=v_r` | `validity-gap` | `install` |
| `s=e=1`, `kappa=0`, `v_p==v_r` | `both-aligned` | `install` |

`boundary` is `in-question` when the host catalog already answers this
question, and `new-question` otherwise. A `new-question` card may still be
`install`. It is ranked last. Opening it is a human decision. It is not
alignment debt, and this run does not build it.

## Placement

Ask the placement questions (`alignment-rules.md` §Placement) only when
`action` is `install`. An install card has these fields and no others in
`placement`:

| field | required content |
|---|---|
| `target` | `extend:<host id>`, `new-skill:<id>`, `tool:<id>`, `script:<host skill id>`, or `runner` |
| `question` | the one question a caller would ask |
| `input` | the one input contract |
| `validity` | the invalidation clause a side actually stated. If neither side stated one, the value is `none stated`. Do not invent one |
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

Priority orders `install` cards only: fix-wrongness (`validity-gap`, and a
five-state `partial` on a question the host already answers), then
honor-promise (a gap the host's own audit already admits), then
`new-question`.

All six labels stay in force on every work. A run that happens to hit only
two of them does not narrow the table.

## Projection tables

Do not copy a card back into either projection gap table, and do not merge
those two tables into one. `joins.paper` and `joins.repo` record which
projection ids this product absorbed.
