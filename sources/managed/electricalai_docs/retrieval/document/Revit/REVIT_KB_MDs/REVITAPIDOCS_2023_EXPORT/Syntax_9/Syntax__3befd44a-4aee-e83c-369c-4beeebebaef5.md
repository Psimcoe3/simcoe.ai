[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPredefinedOptions Method

---



|  |
| --- |
| [DGNExportOptions Class](deca8dc2-439f-9567-9c60-70961b3f7c14.htm)   [See Also](#seeAlsoToggle) |

Returns an instance DGNExportOptions containing settings from a predefined export setup.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static DGNExportOptions GetPredefinedOptions( 	Document document, 	string setup ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetPredefinedOptions ( _ 	document As Document, _ 	setup As String _ ) As DGNExportOptions ``` |

 

| Visual C++ |
| --- |
| ``` public: static DGNExportOptions^ GetPredefinedOptions( 	Document^ document,  	String^ setup ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     A Revit project document to retrieve the setup from.

setup
:   Type:  System String    
     The name of a predefined export setup from the specified document.

#### Return Value

An instance of predefined DGNExportOptions, or    a null reference (  Nothing  in Visual Basic)  if the name was not found.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DGNExportOptions Class](deca8dc2-439f-9567-9c60-70961b3f7c14.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)