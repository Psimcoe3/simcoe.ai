namespace Revit.SDK.Samples.CoordinationModels.CS
{
   partial class CategoriesForm
   {
      /// <summary>
      /// Required designer variable.
      /// </summary>
      private System.ComponentModel.IContainer components = null;

      /// <summary>
      /// Clean up any resources being used.
      /// </summary>
      /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
      protected override void Dispose(bool disposing)
      {
         if (disposing && (components != null))
         {
            components.Dispose();
         }
         base.Dispose(disposing);
      }

      #region Windows Form Designer generated code

      /// <summary>
      /// Required method for Designer support - do not modify
      /// the contents of this method with the code editor.
      /// </summary>
      private void InitializeComponent()
      {
         Categories = new System.Windows.Forms.ListBox();
         label1 = new System.Windows.Forms.Label();
         OK = new System.Windows.Forms.Button();
         Cancel = new System.Windows.Forms.Button();
         SuspendLayout();
         // 
         // Categories
         // 
         Categories.FormattingEnabled = true;
         Categories.ItemHeight = 25;
         Categories.Location = new System.Drawing.Point(39, 74);
         Categories.Name = "Categories";
         Categories.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended;
         Categories.Size = new System.Drawing.Size(515, 704);
         Categories.TabIndex = 0;
         // 
         // label1
         // 
         label1.AutoSize = true;
         label1.Location = new System.Drawing.Point(39, 22);
         label1.Name = "label1";
         label1.Size = new System.Drawing.Size(304, 25);
         label1.TabIndex = 1;
         label1.Text = "Please select one or more categories:";
         // 
         // OK
         // 
         OK.DialogResult = System.Windows.Forms.DialogResult.OK;
         OK.Location = new System.Drawing.Point(305, 804);
         OK.Name = "OK";
         OK.Size = new System.Drawing.Size(112, 34);
         OK.TabIndex = 2;
         OK.Text = "&OK";
         OK.UseVisualStyleBackColor = true;
         OK.Click += OK_Click;
         // 
         // Cancel
         // 
         Cancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
         Cancel.Location = new System.Drawing.Point(442, 804);
         Cancel.Name = "Cancel";
         Cancel.Size = new System.Drawing.Size(112, 34);
         Cancel.TabIndex = 3;
         Cancel.Text = "&Cancel";
         Cancel.UseVisualStyleBackColor = true;
         Cancel.Click += Cancel_Click;
         // 
         // CategoriesForm
         // 
         AutoScaleDimensions = new System.Drawing.SizeF(10F, 25F);
         AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
         ClientSize = new System.Drawing.Size(601, 861);
         Controls.Add(Cancel);
         Controls.Add(OK);
         Controls.Add(label1);
         Controls.Add(Categories);
         Name = "CategoriesForm";
         Text = "Form1";
         ResumeLayout(false);
         PerformLayout();
      }

      #endregion

      private System.Windows.Forms.ListBox Categories;
      private System.Windows.Forms.Label label1;
      private System.Windows.Forms.Button OK;
      private System.Windows.Forms.Button Cancel;
   }
}