[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetTessellationSettings Method

---



|  |
| --- |
| [STLExportOptions Class](c8870dfe-9259-4981-4545-a6c0d0440552.htm)   [See Also](#seeAlsoToggle) |

Sets all the tessellation parameters to its predefined values for the given resolution type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` [ObsoleteAttribute("This method is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use 'setTessellationSettings(ExportResolution::Enum)' method instead.")] public void SetTessellationSettings( 	STLExportResolution resolutionType ) ``` |

 

| Visual Basic |
| --- |
| ``` <ObsoleteAttribute("This method is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use 'setTessellationSettings(ExportResolution::Enum)' method instead.")> _ Public Sub SetTessellationSettings ( _ 	resolutionType As STLExportResolution _ ) ``` |

 

| Visual C++ |
| --- |
| ``` [ObsoleteAttribute(L"This method is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use 'setTessellationSettings(ExportResolution::Enum)' method instead.")] public: void SetTessellationSettings( 	STLExportResolution resolutionType ) ``` |

#### Parameters

resolutionType
:   Type:  [Autodesk.Revit.DB STLExportResolution](75acb45f-3855-9a37-84ac-3f9b3e37fd23.htm)    
     Type of STL exporting resolution.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[STLExportOptions Class](c8870dfe-9259-4981-4545-a6c0d0440552.htm)

[SetTessellationSettings Overload](13450b59-e14c-0024-c16b-61f3bd2efa08.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)