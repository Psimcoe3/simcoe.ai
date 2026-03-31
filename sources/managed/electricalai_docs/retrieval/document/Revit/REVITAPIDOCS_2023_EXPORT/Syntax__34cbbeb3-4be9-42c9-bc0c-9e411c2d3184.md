[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RevitLinkFileName Property

---



|  |
| --- |
| [IFCImportOptions Class](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm)   [See Also](#seeAlsoToggle) |

The full path of the intermediate Revit file created during a previous link action. This is used during "Reload From" to determine the path to the previous generated Revit file.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public string RevitLinkFileName { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property RevitLinkFileName As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ RevitLinkFileName { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[IFCImportOptions Class](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)