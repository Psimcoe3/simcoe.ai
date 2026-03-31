[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DesignToFabricationMappingResult Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Possible results from setting the mapping from Family symbols to Fabrication part types.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public enum DesignToFabricationMappingResult ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration DesignToFabricationMappingResult ``` |

 

| Visual C++ |
| --- |
| ``` public enum class DesignToFabricationMappingResult ``` |

# Members

| Member name | Description |
| --- | --- |
| Success | Setting the mappings for conversion was successful. |
| Undefined | Failed because the map contained no entries. |
| InvalidFamilySymbol | Failed because there was an invalid Family symbol identifier or an identifier that did not exist in the mappings. |
| InvalidFabricationPartType | Failed because there was an invalid Fabrication part type identifier or an identifier that did not exist in the mappings. |
| UnsupportedFamilySymbol | Failed due to attempting to convert an unsupported Family symbol. It is expected to be either valve, strainer, damper, smoke detector, end cap, or other in line component. |
| UnsupportedFabricationPartType | Failed due to attempting to convert an unsupported Fabrication part type. It is expected to be either valve, strainer, damper, smoke detector, end cap, or other in line component. |

# See Also

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)