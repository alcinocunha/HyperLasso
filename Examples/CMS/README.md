# Conference Management System

## Example analyses

| Property     | Bound | Models | Result   |
|--------------|-------|--------|----------|
| `cms_ni_2x2.hq` | 6 | `cms_deterministic_2x2.smv` | UNSAT |
| `cms_ni_2x2.hq` | 5 | `cms_same_paper_2x2.smv` | UNSAT |
| `cms_ni_2x2.hq` | 6 | `cms_same_paper_2x2.smv` | SAT |
| `cms_ni_2x2.hq` | 4 | `cms_any_paper_2x2.smv` | UNSAT |
| `cms_ni_2x2.hq` | 5 | `cms_any_paper_2x2.smv` | SAT |
| `cms_gni_3x2.hq` | 7 | `cms_deterministic_assigns_3x2.smv` | UNSAT |
| `cms_gni_3x2.hq` | 7 | `cms_same_paper_assigns_3x2.smv` | UNSAT |
| `cms_gni_3x2.hq` | 6 | `cms_any_paper_assigns_3x2.smv` | UNSAT |
| `cms_gni_3x2.hq` | 7 | `cms_any_paper_assigns_3x2.smv` | SAT |
| `equivalence_2x2.hq` | 4 | `cms_deterministic_2x2.smv` `cms_same_paper_2x2.smv` | UNSAT |
| `equivalence_2x2.hq` | 3 | `cms_same_paper_2x2.smv` `cms_deterministic_2x2.smv` | UNSAT |
| `equivalence_2x2.hq` | 4 | `cms_same_paper_2x2.smv` `cms_deterministic_2x2.smv` | SAT |
| `equivalence_2x2.hq` | 4 | `cms_same_paper_2x2.smv` `cms_any_paper_2x2.smv` | UNSAT |
| `equivalence_2x2.hq` | 3 | `cms_any_paper_2x2.smv` `cms_same_paper_2x2.smv` | UNSAT |
| `equivalence_2x2.hq` | 4 | `cms_any_paper_2x2.smv` `cms_same_paper_2x2.smv` | SAT |
| `equivalence_3x2.hq` | 5 | `cms_deterministic_assigns_2x2.smv` `cms_deterministic_2x2.smv` | UNSAT |
| `equivalence_3x2.hq` | 5 | `cms_deterministic_2x2.smv` `cms_deterministic_assigns_2x2.smv` | UNSAT |