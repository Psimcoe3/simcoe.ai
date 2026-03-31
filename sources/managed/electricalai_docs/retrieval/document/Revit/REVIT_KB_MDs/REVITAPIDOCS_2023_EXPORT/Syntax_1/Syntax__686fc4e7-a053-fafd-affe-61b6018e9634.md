[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetPresentationMode Method

---



|  |
| --- |
| [RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)   [See Also](#seeAlsoToggle) |

Sets the presentation mode for this rebar set when displayed in the given view.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void SetPresentationMode( 	View dBView, 	RebarPresentationMode presentationMode ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetPresentationMode ( _ 	dBView As View, _ 	presentationMode As RebarPresentationMode _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetPresentationMode( 	View^ dBView,  	RebarPresentationMode presentationMode ) ``` |

#### Parameters

dBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view.

presentationMode
:   Type:  [Autodesk.Revit.DB.Structure RebarPresentationMode](84cfa6b2-460d-9d32-1f6a-55dbbfece098.htm)    
     The presentation mode.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This rebar cannot have a presentation mode applied for dBView, as the view is not valid for rebar presentation, or the orientation of the view matches the normal direction of the rebar. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)