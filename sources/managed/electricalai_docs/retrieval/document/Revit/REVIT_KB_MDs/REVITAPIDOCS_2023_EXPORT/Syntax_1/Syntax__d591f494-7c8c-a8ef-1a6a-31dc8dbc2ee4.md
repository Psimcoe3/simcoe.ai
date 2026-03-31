[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetItem Method

---



|  |
| --- |
| [RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)   [See Also](#seeAlsoToggle) |

Gets the item stored in the RebarContainer at the associated index.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public RebarContainerItem GetItem( 	int itemIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetItem ( _ 	itemIndex As Integer _ ) As RebarContainerItem ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarContainerItem^ GetItem( 	int itemIndex ) ``` |

#### Parameters

itemIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Item index in the Rebar Container

#### Return Value

Rebar Container Item

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The item index is either less than 0 or graeter than or equal to number of items in this Rebar Container element. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)