[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementOnPhaseStatus Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

The statuses that an element can have with respect to a given phase.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public enum ElementOnPhaseStatus ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ElementOnPhaseStatus ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ElementOnPhaseStatus ``` |

# Members

| Member name | Description |
| --- | --- |
| None | Phase status is undefined (e.g., for annotations) |
| Past | Created and demolished before the given phase |
| Existing | Created in a previous phase, existing through the end of the given phase |
| Demolished | Created before the given phase, to be demolished on the given phase |
| New | Created on this phase (and not demolished) |
| Temporary | Created and demolished during this phase |
| Future | Created after this phase |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)