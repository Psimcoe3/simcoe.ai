[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPredefinedSetupNames Method

---



|  |
| --- |
| [DGNExportOptions Class](deca8dc2-439f-9567-9c60-70961b3f7c14.htm)   [See Also](#seeAlsoToggle) |

Returns a list of names of predefined setups of DGN export options.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static IList<string> GetPredefinedSetupNames( 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetPredefinedSetupNames ( _ 	document As Document _ ) As IList(Of String) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<String^>^ GetPredefinedSetupNames( 	Document^ document ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     A Revit document to retrieve names from.

#### Return Value

An array of strings representing names of predefined setups.

# Remarks

To get predefined options in the desired format use the static method getPredefinedOptions defined in DGNExportOptions.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DGNExportOptions Class](deca8dc2-439f-9567-9c60-70961b3f7c14.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)