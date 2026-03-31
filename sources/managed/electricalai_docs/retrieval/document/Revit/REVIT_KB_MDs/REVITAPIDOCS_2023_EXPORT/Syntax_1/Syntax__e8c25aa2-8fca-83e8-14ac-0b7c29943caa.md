[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PartialFailureResults Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Possible results of the partial failure from invoking the DesignToFabricationConverter.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public enum PartialFailureResults ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration PartialFailureResults ``` |

 

| Visual C++ |
| --- |
| ``` public enum class PartialFailureResults ``` |

# Members

| Member name | Description |
| --- | --- |
| NotAllPartsConverted | Not all design elements were converted. |
| InvalidConnections | The connections are invalid. |
| HaveOpenConnectors | Converted fabrication parts have open ends. |
| HaveDifferentOffsets | Converted fabrication parts have different offsets. |
| NoMatchingSize | There are no matching sizes found. |

# See Also

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)