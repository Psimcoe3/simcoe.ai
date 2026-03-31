[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasPresentationOverrides Method

---



|  |
| --- |
| [RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)   [See Also](#seeAlsoToggle) |

Identifies if any RebarContainerItem of this RebarContainer has overridden default presentation settings for the given view.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool HasPresentationOverrides( 	View dBView ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function HasPresentationOverrides ( _ 	dBView As View _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool HasPresentationOverrides( 	View^ dBView ) ``` |

#### Parameters

dBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view.

#### Return Value

True if if any RebarContainerItem of this RebarContainer has overridden default presentation settings, false otherwise.

# Remarks

Default presentation settings can be overriden using  [!:Autodesk::Revit::DB::Structure::RebarContainerItem::SetBarHiddenStatus]  ,  [!:Autodesk::Revit::DB::Structure::RebarContainerItem::SetPresentationMode]  methods

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)