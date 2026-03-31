[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TessellatedShapeBuilderFallback Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Describes what  TessellatedShapeBuilder  function should do, if it cannot build a requested  [TessellatedShapeBuilderTarget](c445e799-cb1d-a4cb-5333-719f5c19df18.htm)  .

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public enum TessellatedShapeBuilderFallback ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration TessellatedShapeBuilderFallback ``` |

 

| Visual C++ |
| --- |
| ``` public enum class TessellatedShapeBuilderFallback ``` |

# Members

| Member name | Description |
| --- | --- |
| Abort | Do nothing. |
| Salvage | Ignore invalid data, and use all valid data. Note that if a complete set of data describes a solid and some data are ignored, then the result will be a sheet and not a solid. |
| Mesh | If a requested geometrical object cannot be built using all data from the face set(s), create a mesh while using as much data from the face set(s) as possible. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)