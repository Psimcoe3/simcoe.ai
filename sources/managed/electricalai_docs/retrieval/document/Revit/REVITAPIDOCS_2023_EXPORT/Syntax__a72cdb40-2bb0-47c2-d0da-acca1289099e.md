[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveItem Method

---



|  |
| --- |
| [RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)   [See Also](#seeAlsoToggle) |

Removes Item from the Rebar Container.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void RemoveItem( 	RebarContainerItem pItem ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveItem ( _ 	pItem As RebarContainerItem _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveItem( 	RebarContainerItem^ pItem ) ``` |

#### Parameters

pItem
:   Type:  [Autodesk.Revit.DB.Structure RebarContainerItem](764f647c-9c3e-b971-1c44-b63f756e1448.htm)    
     Item to be removed from this Rebar Container

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The item is not a member of this Rebar Container element. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)