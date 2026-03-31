[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsInside Method (UV)

---



|  |
| --- |
| [Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the specified point is within this face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public bool IsInside( 	UV point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsInside ( _ 	point As UV _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsInside( 	UV^ point ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     The parameters to be evaluated, in natural parameterization of the face.

#### Return Value

True if point is within this face or on its boundary, otherwise false.

# See Also

[Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)

[IsInside Overload](48a28e26-dd46-5251-c76f-8f2f93d252e9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)