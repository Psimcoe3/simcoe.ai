---
id: revit-family-reference
title: Revit Family Reference
summary: Present Revit answers with explicit family, type, subcategory, and catalog fields.
aliases:
  - revit
  - family type
  - family and type
tags:
  - family
  - type
  - manufacturer
  - part number
route_fit:
  - text
  - retrieval
  - deterministic_tool
triggers:
  - revit
  - family type
  - family and type
  - subcategory
  - manufacturer
  - part number
use_when:
  - The user wants grounded Revit family or type metadata.
  - The answer should preserve exact family/type naming from source records.
avoid_when:
  - The request is unrelated to BIM, Revit, or catalog metadata.
---
When the user asks about Revit family data:

- Prefer exact family and type labels from grounded records.
- Surface manufacturer, part number, lookup key, and catalog identifiers when present.
- If the requested family or type is missing from grounded data, say it is missing instead of inferring it.
- Keep entity names verbatim to avoid near-match confusion.