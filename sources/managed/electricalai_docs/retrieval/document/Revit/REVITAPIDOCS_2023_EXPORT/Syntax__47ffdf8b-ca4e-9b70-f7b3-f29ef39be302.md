[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddinFolder Property

---



|  |
| --- |
| [DocumentEntryPoint Class](99996ba9-d1a7-d27e-c0ce-eb271a4c35bb.htm)   [See Also](#seeAlsoToggle) |

The full path to the Revit Macros module.

**Namespace:**   [Autodesk.Revit.DB.Macros](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

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

[DocumentEntryPoint Class](99996ba9-d1a7-d27e-c0ce-eb271a4c35bb.htm)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)