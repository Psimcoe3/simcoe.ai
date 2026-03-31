[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetGraphicOverrides Method (CheckoutStatus)

---



|  |
| --- |
| [WorksharingDisplaySettings Class](ec25e291-6582-7e8c-f273-efc0c391bcc4.htm)   [See Also](#seeAlsoToggle) |

Returns the graphic overrides associated with a particular ownership status.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public WorksharingDisplayGraphicSettings GetGraphicOverrides( 	CheckoutStatus ownershipStatus ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetGraphicOverrides ( _ 	ownershipStatus As CheckoutStatus _ ) As WorksharingDisplayGraphicSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: WorksharingDisplayGraphicSettings^ GetGraphicOverrides( 	CheckoutStatus ownershipStatus ) ``` |

#### Parameters

ownershipStatus
:   Type:  [Autodesk.Revit.DB CheckoutStatus](f6f6e300-5a37-7e44-7ee1-8dc0c016778a.htm)    
     The ownership status of interest.

#### Return Value

Returns the graphic overrides assigned to a particular ownership status.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[WorksharingDisplaySettings Class](ec25e291-6582-7e8c-f273-efc0c391bcc4.htm)

[GetGraphicOverrides Overload](ce69efb3-a7da-166e-5f00-c306236de4b5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)