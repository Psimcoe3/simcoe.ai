[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetThermalProperties Method

---



|  |
| --- |
| [FamilySymbol Class](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)   [See Also](#seeAlsoToggle) |

Sets the thermal properties for the given FamilySymbol.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetThermalProperties( 	FamilyThermalProperties thermalProperties ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetThermalProperties ( _ 	thermalProperties As FamilyThermalProperties _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetThermalProperties( 	FamilyThermalProperties^ thermalProperties ) ``` |

#### Parameters

thermalProperties
:   Type:  [Autodesk.Revit.DB FamilyThermalProperties](9d9b2125-8398-9b55-8219-cbda4456ab7b.htm)    
     The new thermal properties. If    a null reference (  Nothing  in Visual Basic)  , this unsets custom thermal properties for this FamilySymbol.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The thermal properties are not valid for assignment. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FamilySymbol does not contain thermal properties. |

# See Also

[FamilySymbol Class](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)