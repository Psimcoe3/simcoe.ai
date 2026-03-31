[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Remove Method (ICollection(ElementId))

---



|  |
| --- |
| [MEPSystem Class](65946955-8638-fafb-2657-ef7cb7b2941b.htm)   [See Also](#seeAlsoToggle) |

Remove elements from system.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual void Remove( 	ICollection<ElementId> elementIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Sub Remove ( _ 	elementIds As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Remove( 	ICollection<ElementId^>^ elementIds ) ``` |

#### Parameters

elementIds
:   Type:  [System.Collections.Generic ICollection](http://msdn2.microsoft.com/en-us/library/92t2ye13)   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The elements to be removed from the system.

# Remarks

It is forbidden to remove all terminal elements from system. Terminal elements will be removed from the system automatically after removing this system from document.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument elements is    a null reference (  Nothing  in Visual Basic)  , or any element in that collection is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when some of the elements can't be removed, or when trying to remove all elements from the system. The element which connect to the base equipment can't be removed, |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the operation failed. |

# See Also

[MEPSystem Class](65946955-8638-fafb-2657-ef7cb7b2941b.htm)

[Remove Overload](b7ea3283-b3ff-ec92-c300-f04fde48cfa7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)