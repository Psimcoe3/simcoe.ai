[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetControlPoints Method

---



|  |
| --- |
| [Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)   [See Also](#seeAlsoToggle) |

Given an edge or a curve or a face, return all control points lying on it (in form of geometry references).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ReferenceArray GetControlPoints( 	Reference curveOrEdgeOrFaceReference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetControlPoints ( _ 	curveOrEdgeOrFaceReference As Reference _ ) As ReferenceArray ``` |

 

| Visual C++ |
| --- |
| ``` public: ReferenceArray^ GetControlPoints( 	Reference^ curveOrEdgeOrFaceReference ) ``` |

#### Parameters

curveOrEdgeOrFaceReference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The reference of an edge or curve or face.

#### Return Value

Reference array containing all control points lying on it.

# See Also

[Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)