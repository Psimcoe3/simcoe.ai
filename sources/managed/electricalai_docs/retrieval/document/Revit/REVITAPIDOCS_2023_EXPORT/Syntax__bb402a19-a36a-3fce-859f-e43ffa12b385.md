[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UpdaterId Constructor

---



|  |
| --- |
| [UpdaterId Class](16a9604f-51bd-ce34-f145-17ae06b7c1cf.htm)   [See Also](#seeAlsoToggle) |

creates an instance of UpdaterId for given AddInId and a given GUID value

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public UpdaterId( 	AddInId addInId, 	Guid val ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	addInId As AddInId, _ 	val As Guid _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: UpdaterId( 	AddInId^ addInId,  	Guid val ) ``` |

#### Parameters

addInId
:   Type:  [Autodesk.Revit.DB AddInId](31859d69-72c7-03fb-83e1-5c7719dca253.htm)    
     Id of addin that registers an Updater

val
:   Type:  System Guid    
     a GUID identifying the Updater within addin

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | addInId is not valid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[UpdaterId Class](16a9604f-51bd-ce34-f145-17ae06b7c1cf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)