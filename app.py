import os

def create_project_structure(project_name):
    """
    Creates the necessary folder structure for a Smart Tomcat project.
    
    Args:
        project_name (str): The name of the main project folder.
    """
    print(f"Creating project folder '{project_name}'...")
    
    # Define the required directory paths
    base_dir = project_name
    
    # Updated to include the com/example package structure
    src_java_dir = os.path.join(base_dir, 'src', 'main', 'java', 'com', 'example')
    
    webapp_dir = os.path.join(base_dir, 'src', 'main', 'webapp')
    resources_dir = os.path.join(base_dir, 'src', 'main', 'resources')
    web_inf_dir = os.path.join(base_dir, 'src', 'main', 'webapp', 'WEB-INF')

    try:
        # Create all directories in one go using os.makedirs
        os.makedirs(src_java_dir, exist_ok=True)
        os.makedirs(webapp_dir, exist_ok=True)
        os.makedirs(resources_dir, exist_ok=True)
        os.makedirs(web_inf_dir, exist_ok=True)

        print("Folder structure created successfully:")
        print(f"  - {src_java_dir}")
        print(f"  - {webapp_dir}")
        print(f"  - {resources_dir}")
        print(f"  - {web_inf_dir}")
        return True
    except OSError as e:
        print(f"Error creating directories: {e}")
        return False

def create_default_files(project_name):
    """
    Creates a default Java, JSP, and HTML file with boilerplate content.
    
    Args:
        project_name (str): The name of the main project folder.
        
    Returns:
        A dictionary mapping default filenames to their full paths.
    """
    base_dir = project_name
    
    # Define default file names and content
    java_file_name = "MyServlet.java"
    jsp_file_name = "index.jsp"
    html_file_name = "index.html"

    # Define file paths. Updated to include the package path.
    java_file_path = os.path.join(base_dir, 'src', 'main', 'java', 'com', 'example', java_file_name)
    jsp_file_path = os.path.join(base_dir, 'src', 'main', 'webapp', jsp_file_name)
    html_file_path = os.path.join(base_dir, 'src', 'main', 'webapp', html_file_name)

    # Boilerplate content. Updated to include the package statement.
    java_content = """package com.example;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/MyServlet")
public class MyServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        response.getWriter().append("Hello from MyServlet!");
    }
}
"""
    jsp_content = """<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JSP Page</title>
</head>
<body>
    <h1>Hello from JSP!</h1>
    <p>This is a sample JSP file.</p>
</body>
</html>
"""
    html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>HTML Page</title>
</head>
<body>
    <h1>Hello from HTML!</h1>
    <p>This is a sample HTML file.</p>
</body>
</html>
"""
    
    try:
        # Write files with the default content
        with open(java_file_path, 'w') as f:
            f.write(java_content)
        with open(jsp_file_path, 'w') as f:
            f.write(jsp_content)
        with open(html_file_path, 'w') as f:
            f.write(html_content)

        print("Default files created:")
        print(f"  - {java_file_path}")
        print(f"  - {jsp_file_path}")
        print(f"  - {html_file_path}")

        # Return a dictionary of the created file paths
        return {
            java_file_name: java_file_path,
            jsp_file_name: jsp_file_path,
            html_file_name: html_file_path
        }

    except IOError as e:
        print(f"Error creating files: {e}")
        return {}


def rename_files_prompt(files_to_rename):
    """
    Prompts the user to rename the created files.
    
    Args:
        files_to_rename (dict): A dictionary of default filenames and their paths.
    """
    if not files_to_rename:
        return

    print("\nDo you want to rename any of the created files? (yes/no)")
    choice = input("> ").strip().lower()

    if choice == 'yes':
        for default_name, current_path in files_to_rename.items():
            print(f"\nDo you want to rename '{default_name}'? (yes/no)")
            rename_choice = input("> ").strip().lower()

            if rename_choice == 'yes':
                new_name = input(f"Enter the new name for '{default_name}': ")
                
                # Check for file extension
                current_ext = os.path.splitext(default_name)[1]
                new_ext = os.path.splitext(new_name)[1]

                # If new name doesn't have the correct extension, add it
                if not new_ext or new_ext != current_ext:
                    print(f"New filename must end with '{current_ext}'. Appending extension...")
                    new_name += current_ext
                
                new_path = os.path.join(os.path.dirname(current_path), new_name)

                try:
                    os.rename(current_path, new_path)
                    print(f"File successfully renamed from '{default_name}' to '{new_name}'.")
                except OSError as e:
                    print(f"Error renaming file: {e}")
    else:
        print("Okay, keeping the default filenames.")


def main():
    """
    Main function to run the project generator.
    """
    print("--- Smart Tomcat Project Generator ---")
    project_name = input("Enter the name for your project folder: ")

    if not project_name:
        print("Project name cannot be empty. Exiting.")
        return

    if create_project_structure(project_name):
        created_files = create_default_files(project_name)
        rename_files_prompt(created_files)

    print("\nProject setup complete! You can now open the new folder in IntelliJ.")


if __name__ == "__main__":
    main()
