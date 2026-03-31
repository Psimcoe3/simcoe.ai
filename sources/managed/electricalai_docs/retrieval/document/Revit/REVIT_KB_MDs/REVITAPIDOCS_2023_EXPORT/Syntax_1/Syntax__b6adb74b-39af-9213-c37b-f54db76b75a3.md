[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ActiveView Property

---



|  |
| --- |
| [UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)   [See Also](#seeAlsoToggle) |

The currently active view of the currently active document.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public View ActiveView { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ActiveView As View 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property View^ ActiveView { 	View^ get (); 	void set (View^ value); } ``` |

# Remarks

This property is applicable to the currently active document only. Returns    a null reference (  Nothing  in Visual Basic)  if this document doesn't represent the active document.

The active view can only be changed when:

* There is no open transaction.
* [IsModifiable](af884262-3ba2-b0a0-d7ef-f0a49c1bf1bc.htm)  is false.
* [IsReadOnly](7e813a1b-9163-2509-f280-82572598432b.htm)  is false.
* ViewActivating, ViewActivated, and any pre-action of events (such as DocumentSaving or DocumentClosingevents) are not being handled.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting the property: If the 'view' argument is NULL. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting the property:  * If the given view is not a valid view of the document; -or- * If the given view is a template view; -or- * If the given view is an internal view. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting the property:   * If the document is not currently active; -or- * If the document is currently modifiable (i.e. with an active transaction); -or- * If the document is currently in read-only state; -or- * When invoked during either ViewActivating or ViewActivated event; -or- * When invoked during any pre-action kind of event, such as DocumentSaving, DocumentClosing, etc. |

# See Also

[UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)