[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddPushButton Method

---



|  |
| --- |
| [PulldownButton Class](dc0b7036-00c3-865f-1ae1-e2730d997672.htm)   [See Also](#seeAlsoToggle) |

Adds a new pushbutton to the pulldown button and associates it with an ExternalCommand.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public PushButton AddPushButton( 	PushButtonData buttonData ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddPushButton ( _ 	buttonData As PushButtonData _ ) As PushButton ``` |

 

| Visual C++ |
| --- |
| ``` public: PushButton^ AddPushButton( 	PushButtonData^ buttonData ) ``` |

#### Parameters

buttonData
:   Type:  [Autodesk.Revit.UI PushButtonData](a192ae26-cdca-3d36-72cb-51074ccd9fec.htm)    
     An object containing the data needed to construct the pushbutton.

#### Return Value

The newly added pushbutton.

# Remarks

The new button will display its large image if PushButton.LargeImage is set.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when buttonData is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when button with buttonData.Name already exists in the button. |

# See Also

[PulldownButton Class](dc0b7036-00c3-865f-1ae1-e2730d997672.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)