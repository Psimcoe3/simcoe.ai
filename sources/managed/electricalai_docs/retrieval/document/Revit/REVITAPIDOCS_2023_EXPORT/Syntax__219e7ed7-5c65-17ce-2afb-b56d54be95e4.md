[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BendMultiplier Property

---



|  |
| --- |
| [CableTrayType Class](7ff5138f-5bd6-dbf4-3b57-7ee762bbd7af.htm)   [See Also](#seeAlsoToggle) |

Bend multiplier.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double BendMultiplier { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BendMultiplier As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double BendMultiplier { 	double get (); 	void set (double value); } ``` |

# Remarks

This should be positive and less than 3000.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The bend multiplier value should be positive and less than 3000. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[CableTrayType Class](7ff5138f-5bd6-dbf4-3b57-7ee762bbd7af.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)