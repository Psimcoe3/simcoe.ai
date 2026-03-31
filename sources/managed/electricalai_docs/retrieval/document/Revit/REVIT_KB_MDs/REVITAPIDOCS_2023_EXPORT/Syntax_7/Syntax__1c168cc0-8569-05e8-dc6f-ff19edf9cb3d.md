[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Reload Method

---



|  |
| --- |
| [CADLinkType Class](593779f4-d044-ba36-1888-969743ce782a.htm)   [See Also](#seeAlsoToggle) |

Loads or reloads the link from its currently-stored location. If the link is an external resource, Revit will contact the IExternalResourceServer to get the latest version of the link.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public LinkLoadResult Reload() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Reload As LinkLoadResult ``` |

 

| Visual C++ |
| --- |
| ``` public: LinkLoadResult^ Reload() ``` |

#### Return Value

An object containing the ElementId of the link and an enum value indicating any errors which occurred while trying to load.

# Remarks

If the link is currently loaded, any changes made in-memory to the link's shared coordinates will be discarded.

Graphic overrides will be preserved on reload.

If the original view used to bring in this link has been deleted, Revit will cancel the load.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This CADLinkType represents an import and cannot be used as a link. -or- The element "this CADLinkType" is in a read-only document. |

# See Also

[CADLinkType Class](593779f4-d044-ba36-1888-969743ce782a.htm)

[Reload Overload](f5962e1d-a10c-193d-5266-0f4e2ed8504a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)