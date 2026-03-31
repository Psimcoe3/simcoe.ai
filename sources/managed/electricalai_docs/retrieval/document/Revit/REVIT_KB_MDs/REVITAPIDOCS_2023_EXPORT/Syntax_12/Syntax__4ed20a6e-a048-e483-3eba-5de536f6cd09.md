[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanSuppressFirstOrLastBar Method

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

Checks if the first or last bar in rebar set can be hidden in the given view.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public bool CanSuppressFirstOrLastBar( 	View dBView, 	int end ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanSuppressFirstOrLastBar ( _ 	dBView As View, _ 	end As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanSuppressFirstOrLastBar( 	View^ dBView,  	int end ) ``` |

#### Parameters

dBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view in which presentation mode will be applied.

end
:   Type:  System Int32    
     0 for the first bar in rebar set, 1 for the last bar.

#### Return Value

True the first or last bar in rebar set can be hidden for this view, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)