[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MassLevelData Class

---



|  |
| --- |
| [Members](7ad5d221-ce41-42af-c63e-e868e6ae6aa1.htm)   [See Also](#seeAlsoToggle) |

MassLevelData is a conceptual representation of an occupiable floor (Mass Floor) in a conceptual building model. It is defined by associating a particular level with a particular mass element in a Revit project.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` [ObsoleteAttribute("This class is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'EnergyAnalyticalDetailModel' and 'EnergyAnalysisSpace' classes instead.")] public class MassLevelData : Element ``` |

 

| Visual Basic |
| --- |
| ``` <ObsoleteAttribute("This class is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'EnergyAnalyticalDetailModel' and 'EnergyAnalysisSpace' classes instead.")> _ Public Class MassLevelData _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` [ObsoleteAttribute(L"This class is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'EnergyAnalyticalDetailModel' and 'EnergyAnalysisSpace' classes instead.")] public ref class MassLevelData : public Element ``` |

# Remarks

MassLevelData reports metrics, such as floor areas, related to conceptual space planning. MassLevelData contains information, such as ConceptualConstructionType, used as part of the Conceptual Energy Analytical model. The MassLevel data geometry is determined by combining all the geometry of a mass into a single geometry, and then taking the area of intersection with the level of the MassLevelData.

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB.Analysis MassLevelData

# See Also

[MassLevelData Members](7ad5d221-ce41-42af-c63e-e868e6ae6aa1.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)