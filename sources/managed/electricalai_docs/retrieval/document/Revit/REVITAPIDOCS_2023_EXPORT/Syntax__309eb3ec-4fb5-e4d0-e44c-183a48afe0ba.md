[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ToggleButtonData Constructor (String, String)

---



|  |
| --- |
| [ToggleButtonData Class](ca92168b-f675-ce48-f1e3-fd5640762ad8.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of ToggleButtonData, where the ToggleButton will not be associated to an ExternalCommand.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ToggleButtonData( 	string name, 	string text ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	name As String, _ 	text As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ToggleButtonData( 	String^ name,  	String^ text ) ``` |

#### Parameters

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The internal name of the new button.

text
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The user visible text seen on the new button.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when    a null reference (  Nothing  in Visual Basic)  is passed for one or more arguments. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when an empty string is passed for one or more arguments. |

# See Also

[ToggleButtonData Class](ca92168b-f675-ce48-f1e3-fd5640762ad8.htm)

[ToggleButtonData Overload](9799f894-5817-8748-644d-4972567995fc.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)