[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ApplicableSegmentLengthRounding Property

---



|  |
| --- |
| [FabricRoundingManager Class](6a6324cc-a18c-b883-1b1f-f2ad37147842.htm)   [See Also](#seeAlsoToggle) |

The applicable rounding for fabric segments.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public double ApplicableSegmentLengthRounding { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ApplicableSegmentLengthRounding As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ApplicableSegmentLengthRounding { 	double get (); } ``` |

# Remarks

IsActiveOnElement property of ReinforcementSettings RebarRoundingManager has to be true. ApplicableSegmentLengthRounding is meaningless if ReinforcementSettings RebarRoundingManager IsActiveOnElement is false.

# See Also

[FabricRoundingManager Class](6a6324cc-a18c-b883-1b1f-f2ad37147842.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)