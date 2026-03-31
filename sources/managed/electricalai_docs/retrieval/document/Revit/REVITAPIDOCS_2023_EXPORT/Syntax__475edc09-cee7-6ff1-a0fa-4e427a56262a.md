[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BasicFileInfo Class

---



|  |
| --- |
| [Members](f7a75811-b2ec-8b4c-10d3-6ed0eadf4551.htm)   [See Also](#seeAlsoToggle) |

Encapsulates basic information about a Revit file, including worksharing status, Revit version, username and central path.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class BasicFileInfo : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class BasicFileInfo _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class BasicFileInfo : IDisposable ``` |

# Remarks

This class provides a fast access to get basic information without fully opening a Revit file. The  [Extract](05800394-0e43-45f2-6c89-0db484d6a98c.htm)  method can initialize a new instance of this class by providing a full path for Revit file, including project (.rvt) and family (.rfa) files. This class can extract information from files of older formats. If the structure of the BasicFileInfo storage has not changed, it can also extract information from files of newer formats (making the method  [IsSavedInLaterVersion](27a0583a-c2e4-b198-cf60-168f51c07b13.htm)  relevant). However, if the structure of the storage has changed in a newer file format,  [Extract](05800394-0e43-45f2-6c89-0db484d6a98c.htm)  will not be able to extract the information.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB BasicFileInfo

# See Also

[BasicFileInfo Members](f7a75811-b2ec-8b4c-10d3-6ed0eadf4551.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)