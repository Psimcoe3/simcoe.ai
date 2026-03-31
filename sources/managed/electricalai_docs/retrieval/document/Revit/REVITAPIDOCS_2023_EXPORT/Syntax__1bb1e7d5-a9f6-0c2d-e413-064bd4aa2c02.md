[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DivideSystem Method

---



|  |
| --- |
| [MEPSystem Class](65946955-8638-fafb-2657-ef7cb7b2941b.htm)   [See Also](#seeAlsoToggle) |

Divide the phyisical networks in the system and create a new system for each network.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ICollection<ElementId> DivideSystem( 	Document ADoc ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function DivideSystem ( _ 	ADoc As Document _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<ElementId^>^ DivideSystem( 	Document^ ADoc ) ``` |

#### Parameters

ADoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

#### Return Value

The id of new created systems.

# Remarks

This function only works for Hvac and Piping system.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The system is not dividable. |

# See Also

[MEPSystem Class](65946955-8638-fafb-2657-ef7cb7b2941b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)