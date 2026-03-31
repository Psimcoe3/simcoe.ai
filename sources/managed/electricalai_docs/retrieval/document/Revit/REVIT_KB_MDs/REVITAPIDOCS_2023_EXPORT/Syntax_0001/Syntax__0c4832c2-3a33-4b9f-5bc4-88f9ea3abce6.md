[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddCustomHandle Method

---



|  |
| --- |
| [RebarHandlesData Class](7ce5c75a-c1e9-016b-02cf-1118b6fbefad.htm)   [See Also](#seeAlsoToggle) |

Adds a new handle definition to the rebar. This information is set to the rebar after the API execution is finished successfully.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public void AddCustomHandle( 	int customHandleTag ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddCustomHandle ( _ 	customHandleTag As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddCustomHandle( 	int customHandleTag ) ``` |

#### Parameters

customHandleTag
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The tag of the handle. The tag should be different from the previous ones that were added.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | customHandleTag is a duplicate tag. |

# See Also

[RebarHandlesData Class](7ce5c75a-c1e9-016b-02cf-1118b6fbefad.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)