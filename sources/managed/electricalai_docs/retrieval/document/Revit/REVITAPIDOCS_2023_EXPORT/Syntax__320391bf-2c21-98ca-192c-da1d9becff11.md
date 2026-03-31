[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VersionNumber Property

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Return the primary version of the Revit application.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public string VersionNumber { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property VersionNumber As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ VersionNumber { 	String^ get (); } ``` |

# Remarks

This property can be used by your application to find the version of Revit against which your application is running. Based on this information your application can report if it is able to work correctly with that version of Revit.

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)