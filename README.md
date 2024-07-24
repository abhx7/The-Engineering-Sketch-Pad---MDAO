## Engineering Sketch Pad (ESP)

## **Introduction**

ESP is an open-source software suite designed to streamline the entire Multi-Disciplinary Analysis and Optimization (MDAO) process, from conceptual design to detailed analysis. It eliminates the need for multiple, often incompatible, software tools by providing a unified environment for various design tasks.

## **Key Features**

* **Open Source:** Freely available and modifiable for customization.
* **Seamless Integration:** Supports import/export of various file formats and connections to different analysis tools.
* **Robust Geometry Modeling:**
    * Leverages OpenCASCADE for solid modeling foundation.
    * Employs EGADS for creating and manipulating parametric geometry.
    * Handles complex geometries effectively.
* **Multi-fidelity Analysis:** Integrates with low-fidelity and high-fidelity analysis tools.
* **Sensitivity Analysis:** Calculates the sensitivity of design outputs to design parameters, enabling efficient optimization.
* **User-Friendly Interface:** Web-based interface provides a convenient platform for interacting with the design process.

### **Benefits**

* **Improved Design Efficiency:** Eliminates the need for juggling multiple software tools, streamlining the workflow.
* **Reduced Errors:** Seamless data transfer minimizes errors associated with data exchange between different stages.
* **Faster Design Optimization:** Efficient sensitivity analysis facilitates quicker design iterations.
* **Open-source Nature:** Enables customization and wider adoption within the engineering community.

### **Applications**

* **Aerospace Engineering:** Design and optimization of aircraft components like wings and fuselages.
* **Other Engineering Disciplines:** Applicable to any field requiring MDAO processes.

## **ESP Architecture**

* **OpenCASCADE:** Provides the solid modeling foundation.
* **EGADS:** Builds upon OpenCASCADE for parametric geometry creation.
* **OpenCSM:** Links design parameters to geometry within EGADS.
* **ESP:** Web-based interface for user interaction with the design process.
* **CAPS (Computational Aircraft Prototype Syntheses):** Manages information flow between geometry, analysis tools, and the design environment.
* **AIMs (Analysis Interface Modules):** Interface between CAPS and various analysis tools.

### **Step-by-Step Design Process in ESP**

The design process is divided into phases, each focusing on a specific aspect:

1. **Geometry Creation:** Utilize low-fidelity analysis tools (e.g., XFoil, AVL) to define airfoil sections and wings.
2. **Structural Analysis:** Analyze the structural integrity of the design using software like Masstran or MYSTRAN.
3. **Sensitivity Analysis:** Calculate the sensitivity of design outputs (e.g., lift, drag) to design parameters.
4. **Mesh Generation:** Generate surface and volume meshes for CFD analysis.
5. **3D CFD Analysis:** Perform CFD simulations using a solver like SU2.

## **Additional Resources**

* ESP Documentation: [https://acdl.mit.edu/ESP/](https://acdl.mit.edu/ESP/)
* ESP Publications: [https://acdl.mit.edu/ESP/Publications/AIA](https://acdl.mit.edu/ESP/Publications/AIA)
