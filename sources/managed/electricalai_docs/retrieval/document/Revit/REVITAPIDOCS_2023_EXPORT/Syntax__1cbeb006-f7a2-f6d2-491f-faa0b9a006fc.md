[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaterialFunctionAssignment Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Used in class CompoundStructure to specify the function of a layer.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public enum MaterialFunctionAssignment ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration MaterialFunctionAssignment ``` |

 

| Visual C++ |
| --- |
| ``` public enum class MaterialFunctionAssignment ``` |

# Members

| Member name | Description |
| --- | --- |
| None | Priority = 0 This is deprecated and should not be used. |
| Structure | Priority = 1 (highest priority) |
| Substrate | Priority = 2 |
| Insulation | Priority = 3 |
| Finish1 | Priority = 4 |
| Finish2 | Priority = 5 |
| Membrane | A membrane layer must have thickness 0. It is not represented graphically. |
| StructuralDeck | Indicates layer is a structural deck. |

# Remarks

The function is used primarily to determine layer priority which affects how layers of distinct elements interact at a join. Typically, layers penetrate lower priority layers and merge with layers of the same priority.

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)