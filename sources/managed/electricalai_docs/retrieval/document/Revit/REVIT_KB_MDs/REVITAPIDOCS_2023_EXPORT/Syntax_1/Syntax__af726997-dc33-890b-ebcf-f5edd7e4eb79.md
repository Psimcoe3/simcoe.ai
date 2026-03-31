[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Reload Method (CADLinkOptions)

---



|  |
| --- |
| [CADLinkType Class](593779f4-d044-ba36-1888-969743ce782a.htm)   [See Also](#seeAlsoToggle) |

Loads or reloads the link from its currently-stored location. If the link is an external resource, Revit will contact the IExternalResourceServer to get the latest version of the link.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public LinkLoadResult Reload( 	CADLinkOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Reload ( _ 	options As CADLinkOptions _ ) As LinkLoadResult ``` |

 

| Visual C++ |
| --- |
| ``` public: LinkLoadResult^ Reload( 	CADLinkOptions^ options ) ``` |

#### Parameters

options
:   Type:  [Autodesk.Revit.DB CADLinkOptions](a5d5d78c-cc65-c7a5-0bc8-4413156a2114.htm)    
     Options for reloading the link. Options include the ability to preserve graphic overrides on reload.

#### Return Value

An object containing the ElementId of the link and an enum value indicating any errors which occurred while trying to load.

# Remarks

If the link is currently loaded, any changes made in-memory to the link's shared coordinates will be discarded.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This CADLinkType represents an import and cannot be used as a link. -or- The element "this CADLinkType" is in a read-only document. |

# See Also

[CADLinkType Class](593779f4-d044-ba36-1888-969743ce782a.htm)

[Reload Overload](f5962e1d-a10c-193d-5266-0f4e2ed8504a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)