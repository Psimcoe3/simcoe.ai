[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BendFinalLoopOrientationVector Property

---



|  |
| --- |
| [FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)   [See Also](#seeAlsoToggle) |

Direction of local Fabric Sheet Y axis in bending polyline LCS.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public XYZ BendFinalLoopOrientationVector { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property BendFinalLoopOrientationVector As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ BendFinalLoopOrientationVector { 	XYZ^ get (); } ``` |

# Remarks

Note that bending line may be rotated before it is placed in Fabric Sheet local coordinate system. This vector allows to calculate rotation angle or Trf.

# See Also

[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)