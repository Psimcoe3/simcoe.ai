[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### STLExportOptions Constructor (ExportResolution)

---



|  |
| --- |
| [STLExportOptions Class](c8870dfe-9259-4981-4545-a6c0d0440552.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of STLExportOptions with all predefined tessellation settings, depending on export resolution type. Note: in case of Custom resolution type, tessellation settings won't be predefined and will have default values.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public STLExportOptions( 	ExportResolution resolutionType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	resolutionType As ExportResolution _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: STLExportOptions( 	ExportResolution resolutionType ) ``` |

#### Parameters

resolutionType
:   Type:  [Autodesk.Revit.DB ExportResolution](671e963b-c211-17e7-2c26-5d772d34798a.htm)    
     The type of export resolution.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[STLExportOptions Class](c8870dfe-9259-4981-4545-a6c0d0440552.htm)

[STLExportOptions Overload](202b3151-da4b-fbad-08e1-d63e2fb80930.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)