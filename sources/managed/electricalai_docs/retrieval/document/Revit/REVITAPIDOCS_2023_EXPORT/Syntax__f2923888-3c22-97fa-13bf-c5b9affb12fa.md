[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetMinorLayoutAsMaximumSpacing Method

---



|  |
| --- |
| [FabricSheetType Class](892f0ce6-5548-d299-c976-9355ac4109ee.htm)   [See Also](#seeAlsoToggle) |

Sets the major layout pattern as MaximumSpacing, while specifying the needed parameters for this pattern.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetMinorLayoutAsMaximumSpacing( 	double overallLength, 	double majorStartOverhang, 	double majorEndOverhang, 	double spacing ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetMinorLayoutAsMaximumSpacing ( _ 	overallLength As Double, _ 	majorStartOverhang As Double, _ 	majorEndOverhang As Double, _ 	spacing As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetMinorLayoutAsMaximumSpacing( 	double overallLength,  	double majorStartOverhang,  	double majorEndOverhang,  	double spacing ) ``` |

#### Parameters

overallLength
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The entire length of the wire sheet in the major direction.

majorStartOverhang
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The distance from the edge of the sheet to the first wire in the major direction.

majorEndOverhang
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The distance from the last wire to the edge of the sheet in the major direction.

spacing
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The distance between the wires in the minor direction.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for overallLength is not a number -or- The given value for majorStartOverhang is not a number -or- The given value for majorEndOverhang is not a number -or- The given value for spacing is not a number -or- The arguments are not consistent, please specify proper input values. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for overallLength must be greater than 0 and no more than 30000 feet. -or- The given value for majorStartOverhang must be between 0 and 30000 feet. -or- The given value for majorEndOverhang must be between 0 and 30000 feet. -or- The given value for spacing must be greater than 0 and no more than 30000 feet. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[FabricSheetType Class](892f0ce6-5548-d299-c976-9355ac4109ee.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)