[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ServerPath Class

---



|  |
| --- |
| [Members](7f5161f8-d12d-7caf-a903-cd30f99f6b52.htm)   [See Also](#seeAlsoToggle) |

This class represents a path to a Revit Server location, rather than a location on disk or a network drive.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class ServerPath : ModelPath ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ServerPath _ 	Inherits ModelPath ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ServerPath : public ModelPath ``` |

# Remarks

ServerPaths must refer to Revit models.

ServerPaths are relative to the central server location, and are of the form "RSN://{HostNodeName}/{model\_path}".

The {model\_path} portion is a relative path to a Revit model. For example, the following are valid server paths:

* RSN://EXS/hospital.rvt
* RSN://EXS.autodesk.com/Old Files/hotel2.rvt
* RSN://EXS.autodesk.com/Old Files/Last Week/Tuesday\hotel2.rvt

The following would not be valid server paths:

* //EXS/Old Files/.rvt
* EXS/hospital

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ModelPath](40a84c72-e4b8-72ac-2f71-3216c66a11b3.htm)    
  Autodesk.Revit.DB ServerPath

# See Also

[ServerPath Members](7f5161f8-d12d-7caf-a903-cd30f99f6b52.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)