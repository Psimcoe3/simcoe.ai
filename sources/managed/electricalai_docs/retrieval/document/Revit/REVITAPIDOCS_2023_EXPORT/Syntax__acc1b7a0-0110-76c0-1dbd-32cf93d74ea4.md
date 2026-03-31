[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetUIDocumentMacroSecurityOptions Method

---



|  |
| --- |
| [UIMacroManager Class](187bf41e-4d8a-ecaf-d5f6-2579f9290681.htm)   [See Also](#seeAlsoToggle) |

Sets the UI document macro security options.

**Namespace:**   [Autodesk.Revit.UI.Macros](b95f100a-6cb5-12b3-9b2d-01bc661452db.htm)    
  **Assembly:**   RevitAPIUIMacros  (in RevitAPIUIMacros.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static void SetUIDocumentMacroSecurityOptions( 	UIApplication application, 	UIDocumentMacroOptions macroOptions ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub SetUIDocumentMacroSecurityOptions ( _ 	application As UIApplication, _ 	macroOptions As UIDocumentMacroOptions _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void SetUIDocumentMacroSecurityOptions( 	UIApplication^ application,  	UIDocumentMacroOptions macroOptions ) ``` |

#### Parameters

application
:   Type:  [Autodesk.Revit.UI UIApplication](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)    
     The UI application.

macroOptions
:   Type:  [Autodesk.Revit.UI.Macros UIDocumentMacroOptions](58b01732-d76b-ea31-8dd6-a2da7c90106d.htm)    
     The UI document macro security options.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was NULL |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[UIMacroManager Class](187bf41e-4d8a-ecaf-d5f6-2579f9290681.htm)

[Autodesk.Revit.UI.Macros Namespace](b95f100a-6cb5-12b3-9b2d-01bc661452db.htm)