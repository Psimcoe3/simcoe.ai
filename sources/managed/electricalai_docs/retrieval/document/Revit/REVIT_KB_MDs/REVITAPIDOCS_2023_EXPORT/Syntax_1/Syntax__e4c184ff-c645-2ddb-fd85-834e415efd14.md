[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPolyloops Method

---



|  |
| --- |
| [EnergyAnalysisOpening Class](825025c8-342d-46b7-592e-e42d8f8e8336.htm)   [See Also](#seeAlsoToggle) |

Gets the collection of planar polygons describing the opening geometry.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public IList<Polyloop> GetPolyloops() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPolyloops As IList(Of Polyloop) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Polyloop^>^ GetPolyloops() ``` |

#### Return Value

The collection of polygons describing the opening geometry.

# Remarks

A collection of polyloops (planar polygons) describing the opening geometry as described in gbXML. The geometry is currently measured per analytical(center-line).

# See Also

[EnergyAnalysisOpening Class](825025c8-342d-46b7-592e-e42d8f8e8336.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)