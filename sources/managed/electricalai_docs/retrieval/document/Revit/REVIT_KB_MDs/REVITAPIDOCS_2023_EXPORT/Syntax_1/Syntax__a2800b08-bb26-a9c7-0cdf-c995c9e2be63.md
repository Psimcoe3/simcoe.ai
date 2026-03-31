[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetExtraOptions Method

---



|  |
| --- |
| [IFCImportOptions Class](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm)   [See Also](#seeAlsoToggle) |

Set the list of extra options to be passed into the importer. Each entry in the map is a pair of option name and value. Note that any value here will overwrite the other values in the IFCImportOptions, if it has the same name.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public void SetExtraOptions( 	IDictionary<string, string> options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetExtraOptions ( _ 	options As IDictionary(Of String, String) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetExtraOptions( 	IDictionary<String^, String^>^ options ) ``` |

#### Parameters

options
:   Type:  System.Collections.Generic IDictionary   String  ,  String    
     The list of options.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCImportOptions Class](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)