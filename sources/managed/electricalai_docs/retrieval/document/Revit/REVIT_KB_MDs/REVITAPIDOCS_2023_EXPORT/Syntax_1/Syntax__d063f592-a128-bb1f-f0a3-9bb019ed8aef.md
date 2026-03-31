[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetReferencePick Method

---



|  |
| --- |
| [NumberSystem Class](5c027e93-1dff-9a6e-8602-5b3a3da60ada.htm)   [See Also](#seeAlsoToggle) |

Sets the reference pick.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetReferencePick( 	Reference referencePick ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetReferencePick ( _ 	referencePick As Reference _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetReferencePick( 	Reference^ referencePick ) ``` |

#### Parameters

referencePick
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The pick to set.

# Remarks

It is suggested to get the new reference via GetNumberSystemReference() from the host element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The referencePick is not a valid reference. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[NumberSystem Class](5c027e93-1dff-9a6e-8602-5b3a3da60ada.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)