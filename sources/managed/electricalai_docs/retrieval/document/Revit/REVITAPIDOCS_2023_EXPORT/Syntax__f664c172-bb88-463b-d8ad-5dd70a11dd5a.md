[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementReferenceType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Element reference types.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public enum ElementReferenceType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ElementReferenceType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ElementReferenceType ``` |

# Members

| Member name | Description |
| --- | --- |
| REFERENCE\_TYPE\_NONE | The reference is to an element. |
| REFERENCE\_TYPE\_LINEAR | The reference is to a curve or edge. |
| REFERENCE\_TYPE\_SURFACE | The reference is to a face or face region. |
| REFERENCE\_TYPE\_FOREIGN | The reference is to geometry or elements in linked Revit file. |
| REFERENCE\_TYPE\_INSTANCE | The reference is an instance of a symbol. |
| REFERENCE\_TYPE\_CUT\_EDGE | The reference is to a face that was cut (where the original pick was made on the cut edge). |
| REFERENCE\_TYPE\_MESH | The reference is to a mesh. |
| REFERENCE\_TYPE\_SUBELEMENT | The reference is to a subelement. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)