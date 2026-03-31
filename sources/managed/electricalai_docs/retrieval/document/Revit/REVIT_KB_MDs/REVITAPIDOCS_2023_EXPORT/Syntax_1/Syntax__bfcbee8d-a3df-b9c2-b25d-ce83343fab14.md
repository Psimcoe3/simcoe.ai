[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ValidateExportOptions Method

---



|  |
| --- |
| [INavisworksExporter Interface](b389017c-d7af-f0a4-7440-e9dc30f47718.htm)   [See Also](#seeAlsoToggle) |

Determines if the inputs are valid, and returns an error message if not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` bool ValidateExportOptions( 	Document document, 	string folder, 	string name, 	NavisworksExportOptions options, 	out string exceptionMessage ) ``` |

 

| Visual Basic |
| --- |
| ``` Function ValidateExportOptions ( _ 	document As Document, _ 	folder As String, _ 	name As String, _ 	options As NavisworksExportOptions, _ 	<OutAttribute> ByRef exceptionMessage As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` bool ValidateExportOptions( 	Document^ document,  	String^ folder,  	String^ name,  	NavisworksExportOptions^ options,  	[OutAttribute] String^% exceptionMessage ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to export.

folder
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The folder path.

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The file name.

options
:   Type:  [Autodesk.Revit.DB NavisworksExportOptions](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm)    
     The export options.

exceptionMessage
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)   %    
     The message to show in the exception thrown. This is not an end-user visible message, it is a developer message, and does not have to be localized. Ignored if the function returns true.

#### Return Value

True if the options are valid, false otherwise.

# See Also

[INavisworksExporter Interface](b389017c-d7af-f0a4-7440-e9dc30f47718.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)