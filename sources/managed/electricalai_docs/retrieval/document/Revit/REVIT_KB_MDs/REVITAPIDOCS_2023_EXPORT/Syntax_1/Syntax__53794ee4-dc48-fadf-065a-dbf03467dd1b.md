[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDocumentUsingEnergyDataAnalyticalModel Method

---



|  |
| --- |
| [EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)   [See Also](#seeAlsoToggle) |

Get EnergyDataSettings element and if it exists, return result from getCreateAnalyticalModel.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static bool IsDocumentUsingEnergyDataAnalyticalModel( 	Document ccda ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsDocumentUsingEnergyDataAnalyticalModel ( _ 	ccda As Document _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsDocumentUsingEnergyDataAnalyticalModel( 	Document^ ccda ) ``` |

#### Parameters

ccda
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

#### Return Value

Returns true if the Conceptual Energy Analytical Model is enabled, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)