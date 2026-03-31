[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MakeTransientElements Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

This method encapsulates the process of creating transient elements in the document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void MakeTransientElements( 	ITransientElementMaker maker ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub MakeTransientElements ( _ 	maker As ITransientElementMaker _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void MakeTransientElements( 	ITransientElementMaker^ maker ) ``` |

#### Parameters

maker
:   Type:  [Autodesk.Revit.DB ITransientElementMaker](0d213d8b-eace-f2ff-bd02-3bbd948a6dec.htm)    
     An instance of a class that implements the  [ITransientElementMaker](0d213d8b-eace-f2ff-bd02-3bbd948a6dec.htm)  interface. The maker will be called to create element(s) which would become transient.

# Remarks

The method establishes a context within which transient elements will be created and then invokes the given maker object to create the elements. For more information refer to the  [IsTransient](f391d235-555f-6651-99c6-895fc443f8d8.htm)  method.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This Document has an open editing transaction and is accepting changes. -or- This Document is read-only: It cannot be modified. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)