[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddCommandLink Method (TaskDialogCommandLinkId, String, String)

---



|  |
| --- |
| [TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)   [See Also](#seeAlsoToggle) |

Adds a CommandLink associated to the given id, displaying the indicating main and supporting content.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void AddCommandLink( 	TaskDialogCommandLinkId id, 	string mainContent, 	string supportingContent ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddCommandLink ( _ 	id As TaskDialogCommandLinkId, _ 	mainContent As String, _ 	supportingContent As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddCommandLink( 	TaskDialogCommandLinkId id,  	String^ mainContent,  	String^ supportingContent ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.UI TaskDialogCommandLinkId](21d69e07-93bf-18a6-1b76-c7e917edf897.htm)    
     The id of the CommandLink. This corresponds to the value returned by Show() when the link is chosen by the user.

mainContent
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The main content of the CommandLink.

supportingContent
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The main content of the CommandLink.

# Remarks

Parameter mainContent cannot contain newlines.

If the id has already been set to the task dialog, the new CommandLink definition overrides the old one.

CommandLinks will always be shown in the dialog in the order of their ids.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when mainContent is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when mainContent is an empty string. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the mainContent contains newline characters. |

# See Also

[TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)

[AddCommandLink Overload](29d66720-13af-f1f7-0494-80c7ef6de11d.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)