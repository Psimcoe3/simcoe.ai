[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Show Method

---



|  |
| --- |
| [FilterDialog Class](9d0df7ca-0a3d-12b3-26b7-d28752220f59.htm)   [See Also](#seeAlsoToggle) |

Shows the FilterDialog editing dialog to the user.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void Show() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Show ``` |

 

| Visual C++ |
| --- |
| ``` public: void Show() ``` |

# Remarks

If an existing FilterElement id was set during construction of the object or through the FilterToSelect property, that FilterElement will be selected for editing.

If a new filter name was set during construction of the object or through the NewFilterName property, a new ParameterFilterElement will be created and that new element will be selected for editing. If this option was chosen, the id of the explicitly create new filter will be stored in the NewFilterId property.

Note that the user may opt to add, delete or edit any of the available filter elements (or make no changes at all). To monitor which filters have been changed, use other Revit API mechanisms such as Dynamic Update or the DocumentChanged event.

# See Also

[FilterDialog Class](9d0df7ca-0a3d-12b3-26b7-d28752220f59.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)