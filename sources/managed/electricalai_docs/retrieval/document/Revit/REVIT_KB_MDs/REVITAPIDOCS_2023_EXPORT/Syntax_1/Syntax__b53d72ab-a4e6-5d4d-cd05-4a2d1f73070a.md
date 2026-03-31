[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddinFolder Property

---



|  |
| --- |
| [ApplicationEntryPoint Class](7ff0ad2b-7713-ec77-ccc9-8a01fffcf83e.htm)   [See Also](#seeAlsoToggle) |

The full path to the Revit Macros module.

**Namespace:**   [Autodesk.Revit.UI.Macros](b95f100a-6cb5-12b3-9b2d-01bc661452db.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public string AddinFolder { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property AddinFolder As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property String^ AddinFolder { 	String^ get () sealed; } ``` |

#### Implements

 [IEntryPoint AddinFolder](15974d8d-fda8-5837-09e1-b77f44859d50.htm)

# Remarks

This path should be used instead of the .NET GetExecutingAssembly() result, because the Macros module is loaded in such a way to make that result unreliable.

# See Also

[ApplicationEntryPoint Class](7ff0ad2b-7713-ec77-ccc9-8a01fffcf83e.htm)

[Autodesk.Revit.UI.Macros Namespace](b95f100a-6cb5-12b3-9b2d-01bc661452db.htm)