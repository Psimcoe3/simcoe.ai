[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementMulticlassFilter Constructor (IList(Type), Boolean)

---



|  |
| --- |
| [ElementMulticlassFilter Class](acb0ecb3-afcb-4e94-641d-450716e9ac73.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a filter to find elements whose Element subclasses matches any of a given set of input classes, with an option to instead match elements whose Element subclass does not match the list of input classes.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ElementMulticlassFilter( 	IList<Type> typeList, 	bool inverted ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	typeList As IList(Of Type), _ 	inverted As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementMulticlassFilter( 	IList<Type^>^ typeList,  	bool inverted ) ``` |

#### Parameters

typeList
:   Type:  System.Collections.Generic IList   Type    
     The list of Element subclass types to match.

inverted
:   Type:  System Boolean    
     True if the filter should match all elements which are not of the given Element subclass.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One or more input types are not valid subclasses of Element for this filter. -or- One or more of the types do not exist in Revit's native object model. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ElementMulticlassFilter Class](acb0ecb3-afcb-4e94-641d-450716e9ac73.htm)

[ElementMulticlassFilter Overload](428c9795-8287-bcaf-9ca0-0ab297c8e0c3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)