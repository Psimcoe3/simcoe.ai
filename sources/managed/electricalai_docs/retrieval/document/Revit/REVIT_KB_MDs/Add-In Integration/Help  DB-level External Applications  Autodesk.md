---
created: 2026-01-28T20:40:40 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | DB-level External Applications | Autodesk

> ## Excerpt
> Database-level add-ins are External Applications that do not add anything to the Revit UI. DB-level External Applications can be used when the purpose of the application is to assign events and/or updaters to the Revit session.

---
Database-level add-ins are External Applications that do not add anything to the Revit UI. DB-level External Applications can be used when the purpose of the application is to assign events and/or updaters to the Revit session.

To add a DB-level External Application to Revit, you create an object that implements the IExternalDBApplication interface.

The IExternalDBApplication interface has two abstract methods, OnStartup() and OnShutdown(), which you override in your DB-level external application. Revit calls OnStartup() when it starts, and OnShutdown() when it closes. This is very similar to IExternalApplication, but note that these methods return Autodesk.Revit.DB.ExternalDBApplicationResult rather than Autodesk.Revit.UI.Result and use ControlledApplication rather than UIControlledApplication.

<table summary="" id="GUID-F41AB4DF-5585-4FBD-815E-A26FED38889B__TABLE_4CB2B02571DE4121A6E813B4403A7F36"><tbody><tr><td><b>Code Region: IExternalDBApplication OnShutdown() and OnStartup()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>interface</span><span> </span><span>IExternalDBApplication</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ExternalDBApplicationResult</span><span> </span><span>OnStartup</span><span>(</span><span>ControlledApplication</span><span> application</span><span>);</span><span>
        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ExternalDBApplicationResult</span><span> </span><span>OnShutdown</span><span>(</span><span>ControlledApplication</span><span> application</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The ControlledApplication parameter provides access to Revit \[Database Events\](../../Advanced\_Topics/Events/Database\_Events.html). Events and Updaters to which the database-level application will respond can be registered in the OnStartup method.
