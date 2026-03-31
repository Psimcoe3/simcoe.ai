[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HideBubbleInView Method

---



|  |
| --- |
| [DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm)   [See Also](#seeAlsoToggle) |

Hides the bubble in a view. This method does not apply to Reference planes.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void HideBubbleInView( 	DatumEnds datumEnd, 	View view ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub HideBubbleInView ( _ 	datumEnd As DatumEnds, _ 	view As View _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void HideBubbleInView( 	DatumEnds datumEnd,  	View^ view ) ``` |

#### Parameters

datumEnd
:   Type:  [Autodesk.Revit.DB DatumEnds](60cdd5d4-8c6c-320b-7b8b-1cc4487edd9c.htm)    
     The end of the datum plane.

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view on which the DatumPlane shows.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The datum plane cannot be visible in the view. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This datum plane doesn't support bubble operations. |

# See Also

[DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)