[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidUserVisibleFullServerPath Method

---



|  |
| --- |
| [ModelPathUtils Class](f558548a-af73-483e-5428-9419cb70aeb8.htm)   [See Also](#seeAlsoToggle) |

Determines whether the given string represents a valid server path.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool IsValidUserVisibleFullServerPath( 	string strPath ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidUserVisibleFullServerPath ( _ 	strPath As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidUserVisibleFullServerPath( 	String^ strPath ) ``` |

#### Parameters

strPath
:   Type:  System String    
     The path, in string form

#### Return Value

True if the given path is a valid server path, false otherwise.

# Remarks

ServerPaths must refer to Revit models.

ServerPaths are relative to the central server location, and are of the form "RSN://{HostNodeName}/{model\_path}".

The {model\_path} portion is a relative path to a Revit model. For example:

* RSN://EXS/hospital.rvt
* RSN://EXS.autodesk.com/Old Files/hotel2.rvt
* RSN://EXS.autodesk.com/Old Files/Last Week/Tuesday\hotel2.rvt

are all valid server paths.

* //EXS/Old Files/.rvt
* EXS/hospital

are not valid server paths. If this function returns false, it does not necessarily mean the given path is a file path. It may be a malformed string.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ModelPathUtils Class](f558548a-af73-483e-5428-9419cb70aeb8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)