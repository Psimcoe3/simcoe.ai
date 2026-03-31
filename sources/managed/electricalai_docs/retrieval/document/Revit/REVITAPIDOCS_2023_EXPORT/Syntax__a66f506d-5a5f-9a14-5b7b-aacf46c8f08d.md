[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetViewId Method

---



|  |
| --- |
| [ElevationMarker Class](ca59d2f7-4cd0-d13d-22a0-c153ac8310d4.htm)   [See Also](#seeAlsoToggle) |

Returns the ViewSection id for the index of the ElevationMarker.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId GetViewId( 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetViewId ( _ 	index As Integer _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetViewId( 	int index ) ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of the ElevationMarker for which a ViewSection id will be returned.

#### Return Value

ViewSection id of the view at the ElevationMarker index, invalid element id otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The index index is out of range for this ElevationMarker. |

# See Also

[ElevationMarker Class](ca59d2f7-4cd0-d13d-22a0-c153ac8310d4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)