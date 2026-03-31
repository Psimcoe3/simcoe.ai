[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveAllTriggers Method

---



|  |
| --- |
| [UpdaterRegistry Class](4f24f516-5274-1420-f255-458c0af5d318.htm)   [See Also](#seeAlsoToggle) |

Removes all triggers associated with Updater with specified UpdaterId. Does not unregister updater.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static void RemoveAllTriggers( 	UpdaterId id ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub RemoveAllTriggers ( _ 	id As UpdaterId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void RemoveAllTriggers( 	UpdaterId^ id ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.DB UpdaterId](16a9604f-51bd-ce34-f145-17ae06b7c1cf.htm)    
     Id of specified updater

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The updater's owner's AddIn does not match the currently active AddIn. -or- RemoveAllTriggers called while executing an updater. |

# See Also

[UpdaterRegistry Class](4f24f516-5274-1420-f255-458c0af5d318.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)