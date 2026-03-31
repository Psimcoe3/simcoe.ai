[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetThermalProperties Method

---



|  |
| --- |
| [FamilySymbol Class](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)   [See Also](#seeAlsoToggle) |

Gets the thermal properties for the given FamilySymbol.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public FamilyThermalProperties GetThermalProperties() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetThermalProperties As FamilyThermalProperties ``` |

 

| Visual C++ |
| --- |
| ``` public: FamilyThermalProperties^ GetThermalProperties() ``` |

#### Return Value

The thermal properties.    a null reference (  Nothing  in Visual Basic)  if the family symbol does not contain thermal properties.

# Remarks

Doors, windows, and curtain wall panels will have thermal properties.

# See Also

[FamilySymbol Class](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)