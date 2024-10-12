import FreeCAD
import FreeCADGui
import Part
import Mesh

# Load the STL file
mesh = Mesh.Mesh("MK2/STL/MK2_bracket-inlet.stl")

# Create a new document
doc = FreeCAD.newDocument("Render")

# Add the mesh to the document
part = doc.addObject("Mesh::Mesh", "MyMesh")
part.Mesh = mesh

# Set up the view
FreeCADGui.activeDocument().activeView().viewAxonometric()
FreeCADGui.activeDocument().activeView().fitAll()

# Save the view as PNG
FreeCADGui.activeDocument().activeView().saveImage("output_image.png", 1920, 1080, "White")