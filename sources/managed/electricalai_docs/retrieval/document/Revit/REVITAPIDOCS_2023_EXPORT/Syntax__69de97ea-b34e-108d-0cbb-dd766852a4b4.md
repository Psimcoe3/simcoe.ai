[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PushButtonData Constructor

---



|  |
| --- |
| [PushButtonData Class](a192ae26-cdca-3d36-72cb-51074ccd9fec.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of PushButtonData.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public PushButtonData( 	string name, 	string text, 	string assemblyName, 	string className ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	name As String, _ 	text As String, _ 	assemblyName As String, _ 	className As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: PushButtonData( 	String^ name,  	String^ text,  	String^ assemblyName,  	String^ className ) ``` |

#### Parameters

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The internal name of the new button.

text
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The user visible text seen on the new button.

assemblyName
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The assembly path of the button.

className
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The name of the class containing the implementation for the command.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when    a null reference (  Nothing  in Visual Basic)  is passed for one or more arguments. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when an empty string is passed for one or more arguments. |

# See Also

[PushButtonData Class](a192ae26-cdca-3d36-72cb-51074ccd9fec.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)