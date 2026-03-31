[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsPinned Method

---



|  |
| --- |
| [MultistoryStairs Class](8b07cbff-013c-889f-8807-703e63a91923.htm)   [See Also](#seeAlsoToggle) |

Checks if a stair is pinned.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool IsPinned( 	Stairs stairs ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsPinned ( _ 	stairs As Stairs _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsPinned( 	Stairs^ stairs ) ``` |

#### Parameters

stairs
:   Type:  [Autodesk.Revit.DB.Architecture Stairs](45e2c068-7e52-c84a-cfb8-a53c531d28fa.htm)    
     A stairs element in this multistory stairs element.

#### Return Value

Returns true if the stairs is pinned; otherwise returns false.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input stairs is not a member of this multistory stairs. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MultistoryStairs Class](8b07cbff-013c-889f-8807-703e63a91923.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)