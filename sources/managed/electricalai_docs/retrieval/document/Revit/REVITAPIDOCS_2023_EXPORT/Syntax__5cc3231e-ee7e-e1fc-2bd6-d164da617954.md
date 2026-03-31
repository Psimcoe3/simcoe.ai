[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UpdateAllOpenViews Method

---



|  |
| --- |
| [UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)   [See Also](#seeAlsoToggle) |

Update all open views in this document after elements have been changed, deleted, selected or de-selected. Graphics in the views are fully redrawn regardless of which elements have changed.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public void UpdateAllOpenViews() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub UpdateAllOpenViews ``` |

 

| Visual C++ |
| --- |
| ``` public: void UpdateAllOpenViews() ``` |

# Remarks

This function should only rarely be needed, but might be required when working with graphics drawn from outside of Revit's transactions and elements, for example, when using  [IDirectContext3DServer](7709521d-9954-ef80-1f13-3bc6ee660d5d.htm)  . This function is potentially expensive as many views may be updated at once, including regeneration of view's geometry and redisplay of graphics. Thus for most situations it is recommended that API applications rely on the Revit application framework to update views more deliberately.

# See Also

[UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)