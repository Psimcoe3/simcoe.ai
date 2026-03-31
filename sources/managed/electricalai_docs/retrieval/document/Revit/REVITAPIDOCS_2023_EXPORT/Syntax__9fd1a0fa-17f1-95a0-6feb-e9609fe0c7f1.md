[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSubelement Method (String)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Gets the subelement referenced by a unique id string.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public Subelement GetSubelement( 	string uniqueId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSubelement ( _ 	uniqueId As String _ ) As Subelement ``` |

 

| Visual C++ |
| --- |
| ``` public: Subelement^ GetSubelement( 	String^ uniqueId ) ``` |

#### Parameters

uniqueId
:   Type:  System String    
     The unique id that identifies element or subelement.- [UniqueId](f9a9cb77-6913-6d41-ecf5-4398a24e8ff8.htm)

#### Return Value

The subelement referenced by the input argument.

# Remarks

a null reference (  Nothing  in Visual Basic)  will be returned if the input id string doesn't reference to a valid element or subelement.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[GetSubelement Overload](fdd67b30-5d02-e5c4-ebf1-ddcb5382ffc1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)