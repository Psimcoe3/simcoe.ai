[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetTopFaces Method

---



|  |
| --- |
| [HostObjectUtils Class](05539c78-f61a-4e75-0a8a-becb0a66b941.htm)   [See Also](#seeAlsoToggle) |

Returns the top faces for this host object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static IList<Reference> GetTopFaces( 	HostObject hostObject ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetTopFaces ( _ 	hostObject As HostObject _ ) As IList(Of Reference) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<Reference^>^ GetTopFaces( 	HostObject^ hostObject ) ``` |

#### Parameters

hostObject
:   Type:  [Autodesk.Revit.DB HostObject](56a32e0b-df65-a6ba-40bd-8f50a1f31dcd.htm)    
     The host object.

#### Return Value

An array of references to the faces which are at the top of this element.

# Remarks

This utility supports host objects whose top faces represent one of the boundaries of CompoundStructure (such as roofs, floors or ceilings).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This host object does not support access to top or bottom faces. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[HostObjectUtils Class](05539c78-f61a-4e75-0a8a-becb0a66b941.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)