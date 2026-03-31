[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetTransform Method

---



|  |
| --- |
| [AssemblyInstance Class](4e60704c-dfe3-72b6-7892-6440503fa078.htm)   [See Also](#seeAlsoToggle) |

Sets the origin of the assembly instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetTransform( 	Transform trf ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetTransform ( _ 	trf As Transform _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetTransform( 	Transform^ trf ) ``` |

#### Parameters

trf
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     Transform to be set.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | trf is not a rigid body transformation. |

# See Also

[AssemblyInstance Class](4e60704c-dfe3-72b6-7892-6440503fa078.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)