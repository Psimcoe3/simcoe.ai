[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ClassName Property

---



|  |
| --- |
| [PushButtonData Class](a192ae26-cdca-3d36-72cb-51074ccd9fec.htm)   [See Also](#seeAlsoToggle) |

The name of the class containing the implementation for the command.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public string ClassName { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ClassName As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ ClassName { 	String^ get (); 	void set (String^ value); } ``` |

# Remarks

The class name which implements the interface IExternalCommand.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when setting the value to    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when setting the value to an empty string. |

# See Also

[PushButtonData Class](a192ae26-cdca-3d36-72cb-51074ccd9fec.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)