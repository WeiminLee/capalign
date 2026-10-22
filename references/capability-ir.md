# Capability Intermediate Representation (IR)

All inventories — reference (repo / paper / blog) and host agent — normalize into
this one shape. This is what makes alignment possible across heterogeneous sources.

```json
{
  "surface": {
    "label": "to-label",            // repo path / paper title / blog title / host name
    "source_kind": "repo|paper|blog|host",
    "layer": "core|neighborhood",  // default core; neighborhood = identity-gated related work
    "relation": "null|companion-paper|official-docs|sibling|cited-method|declared-related",
    "generated_at": "ISO-8601"
  },
  "capabilities": [
    {
      "id": "kebab-case-unique-id",
      "name": "short human name",
      "type": "compute|tool|skill|workflow|data|interface|concept",
      "description": "one-phrase capability semantics (what it does, not how)",
      "evidence": [
        {"kind": "cli|module|doc|code|method|claim|tool-mention", "location": "path:line | section | URL | quote"}
      ],
      "confidence": "high|medium|low",    // low = inferred, must be flagged in the report
      "layer": "core|neighborhood",       // inherit surface.layer if omitted
      "host_need": ["none"]               // none|data|contract|runner|verification; see §Host need
    }
  ]
}
```

## Type vocabulary

| type | repo | paper | blog | host |
|---|---|---|---|---|
| `compute` | pure computation module/function | an algorithm/formula step | a recipe | local computation tool |
| `tool` | CLI command / MCP tool | a software it uses | a named command | a tool registry entry |
| `skill` | documented procedure | a workflow/protocol | a workflow description | an installed skill |
| `workflow` | multi-step pipeline | end-to-end protocol | a multi-step recipe | a scenario/composite skill |
| `data` | dataset/format produced | tables/figures/products | numbers/benchmarks | a data artifact |
| `interface` | API / file format | IO contract | a format | a transport / MCP server |
| `concept` | design principle | theory/approximation | a claim/opinion | a scientific-decision rule |

## Host need

What the host must own for this capability to be deliverable, given that the
host's capacity is **the agent plus its surface**:

| value | the host must supply |
|---|---|
| `none` | nothing beyond a standard library the agent can call; the agent has a local correctness check |
| `data` | a dataset, database, catalog, or calibrated coefficient the agent cannot synthesize |
| `contract` | a declared artifact, a persisted output, or a reproducible record the user relies on |
| `runner` | credentials, remote compute, a task lifecycle, or a job handle |
| `verification` | a regime someone has checked — measured traps, a validated model, a known-good implementation |

`none` is not "the agent knows the topic". It requires the named local check
(`alignment-rules.md` §Agent competence). A non-empty `host_need` is what makes a
row a real gap.

## Normalization rules
1. Capabilities are **semantic units**, not file counts: a repo with 200 functions and 12
   CLI entry points yields ~10–30 capabilities.
2. `id` is stable for diffing across runs; derive it from name + source kind.
3. `confidence: low` entries are included but must carry an explicit `low` tag — the
   alignment report must not treat them as evidence for "missing".
4. Duplicate mentions collapse into one capability with multiple `evidence` entries.
5. Host inventory additionally records where each capability came from
   (skill dir, tool registry, scripts) so recommendations can point at a concrete host location.
6. Recovered companion paper is a second core surface (`relation: companion-paper`);
   neighborhood items are separate surfaces (`layer: neighborhood`). Do not collapse
   paper-arm and repo-arm capabilities into one row — coverage is reference-conditioned
   (`formal-foundations.md` C3).
7. Neighborhood capabilities are `medium` at most; search-snippet-only evidence is
   `low` and never drives `missing`.

## Granularity boundary (codified from E1 pilot finding F3)

1. A capability is a **user-reachable semantic unit** — something a user can get done
   through the inventoried subject — never a file, function, class, or config count.
2. **CLI / API entry points**: an entry point that merely executes an already-inventoried
   capability merges into that capability's evidence (`kind: cli` / `interface`); an
   entry point that exposes a distinct user-reachable deliverable not otherwise
   documented becomes its own capability.
3. **Dependency fingerprints** are derivation clues, not capabilities: they may suggest
   implied families (marked `medium` until confirmed), never stand as `high` items on
   their own, and never drive a `missing` verdict alone.
4. **Meta-level items** are not inventoried: packaging, dependency lists, the
   framework a CLI is built on, and **generic agent plumbing** (plugin
   marketplace, extra MCP server, lockfile replay, per-environment bootstrap,
   token login, calculator codegen). See `alignment-rules.md` §Scope.
5. **Bounded size**: a typical repo normalizes to ~10–30 capabilities; a larger
   inventory signals over-splitting, a far smaller one signals over-collapsing.
6. **Registry / roster**: a catalog of N models, frameworks, or datasets is one
   `interface` (or `data`) capability when model selection is a domain-agent
   method. Hub install/bootstrap of that catalog is plumbing (rule 4), not a
   verb. Domain-agent verbs on the catalog (benchmark protocol, fine-tune,
   distill) are separate `workflow` capabilities. Roster entries are not
   themselves capabilities and are not neighborhood items.
7. **Default at dispute**: an item whose semantics or evidence are genuinely ambiguous
   is kept as `confidence: low` — low-preserve beats high-pollution; `low` never drives
   a gap class.
8. **Same observable, one compute.** Energy, forces, stress, relaxation, or MD
   produced by a different calculator or Hamiltonian merge into the existing
   `compute` capability. Class `equivalent` if the host already produces that
   quantity. A distinct domain method on top of that quantity (adsorption-energy
   protocol, fine-tune, distill) stays its own `workflow`.
9. **A library is inventoried as workflows, not as a module tree.** A capability
   is a procedure a user runs ("spinodal decomposition", "dendritic growth"),
   not a module, class, or CLI subcommand. Modules and entry points are
   `evidence` pointers for the workflow they serve. Framework internals — mesh,
   linear-solver backend, viewer, file I/O, term algebra — are not capabilities
   at all, the same way a database driver is not a database feature. Counting a
   library's modules as capabilities inflates a host gap table with methods the
   agent already knows.