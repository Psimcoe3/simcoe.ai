[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OnOpenConflict Method

---



|  |
| --- |
| [DefaultOpenFromCloudCallback Class](6269ec13-f36e-64fd-f173-aa7c358912f9.htm)   [See Also](#seeAlsoToggle) |

A method called when the conflict is happen during the model opening.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public virtual OpenConflictResult OnOpenConflict( 	OpenConflictScenario scenario ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function OnOpenConflict ( _ 	scenario As OpenConflictScenario _ ) As OpenConflictResult ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual OpenConflictResult OnOpenConflict( 	OpenConflictScenario scenario ) ``` |

#### Parameters

scenario
:   Type:  [Autodesk.Revit.DB OpenConflictScenario](7db711fa-cfb1-39da-a184-5aaf4230b660.htm)    
     The scenario of the conflict.

#### Return Value

Returns the result to indicate whether to keep the unsynchronized change, or open the latest version or cancel the open action.

#### Implements

 [IOpenFromCloudCallback OnOpenConflict(OpenConflictScenario)](21c8169e-9a58-3a6f-9060-e42975f39b16.htm)

# See Also

[DefaultOpenFromCloudCallback Class](6269ec13-f36e-64fd-f173-aa7c358912f9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)