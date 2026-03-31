[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Commit Method

---



|  |
| --- |
| [AppearanceAssetEditScope Class](743c74ba-12de-4d77-a677-325229525955.htm)   [See Also](#seeAlsoToggle) |

Finishes the edit scope.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public void Commit( 	bool updateOpenViews ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Commit ( _ 	updateOpenViews As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Commit( 	bool updateOpenViews ) ``` |

#### Parameters

updateOpenViews
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     When true, force update of the open views.

# Remarks

All the changes made after starting the EditScope will be committed. Changes will be merged into one transaction. If the appearance asset element is used in one or more materials, they will be updated to match any changes made. Open views may not redraw after changes. View update can be forced with the input argument, but doing so can be an expensive operation. Consider using false if immediate update is not needed or if multiple calls to this method are used in a loop.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | EditScope is not active. EditScope can only be committed or cancelled when it is active. -or- EditScope cannot be closed, there is no opened transaction. -or- The editable asset is not valid. |

# See Also

[AppearanceAssetEditScope Class](743c74ba-12de-4d77-a677-325229525955.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)