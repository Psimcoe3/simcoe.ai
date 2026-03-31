[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IPointCloudEngine Interface

---



|  |
| --- |
| [Members](b3f15ac0-3258-b462-387a-3aaa98259ec3.htm)   [See Also](#seeAlsoToggle) |

An interface that controls the behavior of the link from Revit to a custom Point Cloud Engine.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public interface IPointCloudEngine ``` |

 

| Visual Basic |
| --- |
| ``` Public Interface IPointCloudEngine ``` |

 

| Visual C++ |
| --- |
| ``` public interface class IPointCloudEngine ``` |

# Remarks

An instance of this interface should be created by the engine provider and registered with the PointCloudEnginesRegistry. The engine may associated with a particular file name extension during registration (for example, Revit supplies a built-in engine for working with files with the extension "pcg"). Alternatively, the engine may be associated with an identifier which is not expected to the be the extension of a particular file.

# See Also

[IPointCloudEngine Members](b3f15ac0-3258-b462-387a-3aaa98259ec3.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)