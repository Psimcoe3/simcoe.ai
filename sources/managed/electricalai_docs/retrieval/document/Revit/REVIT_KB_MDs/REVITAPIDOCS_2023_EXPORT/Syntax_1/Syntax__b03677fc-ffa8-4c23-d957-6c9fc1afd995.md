[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsSet Property

---



|  |
| --- |
| [BoundingBoxUV Class](e38a0145-4267-0b3f-0718-adb14e34c94e.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the BoundingBoxUV is set or not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public bool IsSet { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsSet As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsSet { 	bool get (); } ``` |

# Remarks

An unset BoundingBoxUV has its lower-left corner to the right of (and above) its upper-right corner (this is an arbitrary internal representation). It means that it is empty and has never been initialized. If someone using the API creates a Plane via one of the Plane.Create() methods, for example, the Plane will not have its envelope set, so Surface.GetBoundingBoxUV() would return an empty BoundingBoxUV.

# See Also

[BoundingBoxUV Class](e38a0145-4267-0b3f-0718-adb14e34c94e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)