[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMassIds Method

---



|  |
| --- |
| [MassGBXMLExportOptions Class](ac0f3089-3aa2-7dbd-511f-07c4a491df19.htm)   [See Also](#seeAlsoToggle) |

Gets a list of masses to use as shading surfaces in the exported gbXML--these masses must not have mass floors or mass zones so as not to end up with duplicate surface information in the gbXML output.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<ElementId> GetMassIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetMassIds As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ElementId^>^ GetMassIds() ``` |

#### Return Value

The ids of the masses.

# See Also

[MassGBXMLExportOptions Class](ac0f3089-3aa2-7dbd-511f-07c4a491df19.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)