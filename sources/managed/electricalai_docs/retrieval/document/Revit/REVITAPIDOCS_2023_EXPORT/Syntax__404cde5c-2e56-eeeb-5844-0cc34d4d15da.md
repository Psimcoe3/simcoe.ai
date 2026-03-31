[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ApplicableTotalLengthRoundingMethod Property

---



|  |
| --- |
| [FabricRoundingManager Class](6a6324cc-a18c-b883-1b1f-f2ad37147842.htm)   [See Also](#seeAlsoToggle) |

The applicable rounding method for Cut Overall Length and Cut Overall Width parameters.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public RoundingMethod ApplicableTotalLengthRoundingMethod { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ApplicableTotalLengthRoundingMethod As RoundingMethod 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property RoundingMethod ApplicableTotalLengthRoundingMethod { 	RoundingMethod get (); } ``` |

# Remarks

IsActiveOnElement property of ReinforcementSettings FabricRoundingManager has to be true. ApplicableTotalLengthRoundingMethod is meaningless if ReinforcementSettings FabricRoundingManager IsActiveOnElement is false.

# See Also

[FabricRoundingManager Class](6a6324cc-a18c-b883-1b1f-f2ad37147842.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)