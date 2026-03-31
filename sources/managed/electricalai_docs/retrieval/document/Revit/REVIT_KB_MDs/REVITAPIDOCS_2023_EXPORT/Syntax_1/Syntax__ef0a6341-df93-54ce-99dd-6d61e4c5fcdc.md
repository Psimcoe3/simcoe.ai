[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsMergedPart Method

---



|  |
| --- |
| [PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)   [See Also](#seeAlsoToggle) |

Is the Part the result of a merge.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool IsMergedPart( 	Part part ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsMergedPart ( _ 	part As Part _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsMergedPart( 	Part^ part ) ``` |

#### Parameters

part
:   Type:  [Autodesk.Revit.DB Part](1ee04db6-195f-58fa-a245-5a2f2d404200.htm)

#### Return Value

True if the Part is the result of a merge operation.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)