"""
RUBICON INDUSTRY-ORIENTED SKILL DEVELOPMENT AND PLACEMENT TRAINING
Student Management System - Integrated Project
Covers: Python Basics, Data Structures, File Handling, Modules
"""

import os
import datetime
import json
from typing import List, Dict, Set, Tuple, Optional

# ==================== MODULE 1: STUDENT SCORE MANAGEMENT SYSTEM ====================
# Day 1: Python Basics - Lists, Tuples, Sets, Dictionaries

class StudentScoreManagementSystem:
    """Manages student details, courses, skills, and scores"""
    
    def __init__(self):
        self.students: Dict[int, Dict] = {}  # Dictionary to store all students
        self.course_catalog: Tuple = (
            "Python Programming",
            "Data Structures",
            "Web Development",
            "Database Management",
            "Aptitude Training"
        )
    
    def add_student(self, name: str, roll_no: int, scores: Dict[str, int], skills: List[str]) -> Dict:
        """Add a new student to the system"""
        unique_skills = set(skills)  # Set for unique skills
        
        student = {
            "name": name,
            "roll_no": roll_no,
            "course_details": self.course_catalog,  # Tuple for courses
            "skills": skills,  # List for skills
            "unique_skills": unique_skills,  # Set for unique skills
            "scores": scores,  # Dictionary for subject scores
            "total_score": sum(scores.values()),
            "average_score": sum(scores.values()) / len(scores) if scores else 0,
            "registration_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.students[roll_no] = student
        return student
    
    def get_student_by_roll(self, roll_no: int) -> Optional[Dict]:
        """Retrieve student by roll number"""
        return self.students.get(roll_no)
    
    def update_score(self, roll_no: int, subject: str, new_score: int) -> bool:
        """Update a student's score for a specific subject"""
        if roll_no in self.students:
            if subject in self.students[roll_no]["scores"]:
                self.students[roll_no]["scores"][subject] = new_score
                # Recalculate totals
                scores = self.students[roll_no]["scores"]
                self.students[roll_no]["total_score"] = sum(scores.values())
                self.students[roll_no]["average_score"] = sum(scores.values()) / len(scores)
                return True
        return False
    
    def get_top_performers(self, n: int = 3) -> List[Dict]:
        """Get top n students by average score"""
        sorted_students = sorted(
            self.students.values(), 
            key=lambda x: x["average_score"], 
            reverse=True
        )
        return sorted_students[:n]
    
    def display_student_summary(self, roll_no: int):
        """Display detailed student summary"""
        student = self.get_student_by_roll(roll_no)
        if student:
            print("\n" + "="*50)
            print(f"Student: {student['name']} (Roll No: {student['roll_no']})")
            print(f"Registration: {student['registration_date']}")
            print(f"\nCourses Enrolled: {len(student['course_details'])} courses")
            print(f"Skills: {', '.join(student['skills'])}")
            print(f"Unique Skills: {', '.join(student['unique_skills'])}")
            print("\nScore Breakdown:")
            for subject, score in student['scores'].items():
                print(f"  {subject}: {score}")
            print(f"\nTotal Score: {student['total_score']}")
            print(f"Average Score: {student['average_score']:.2f}")
            
            # Grade calculation
            avg = student['average_score']
            if avg >= 90:
                grade = "A+"
            elif avg >= 80:
                grade = "A"
            elif avg >= 70:
                grade = "B+"
            elif avg >= 60:
                grade = "B"
            else:
                grade = "C"
            print(f"Grade: {grade}")
            print("="*50)
        else:
            print(f"No student found with roll number {roll_no}")


# ==================== MODULE 2: FILE HANDLING ====================
# Day 3: File Handling - Save and retrieve data from files

class FileHandler:
    """Handles file operations for student data"""
    
    def __init__(self, filename: str = "student_data.json"):
        self.filename = filename
    
    def save_to_file(self, students: Dict) -> bool:
        """Save student data to JSON file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(students, file, indent=4)
            print(f"✓ Data saved successfully to {self.filename}")
            return True
        except Exception as e:
            print(f"✗ Error saving data: {e}")
            return False
    
    def load_from_file(self) -> Dict:
        """Load student data from JSON file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                print(f"✓ Data loaded successfully from {self.filename}")
                return data
            else:
                print(f"File {self.filename} not found. Starting with empty database.")
                return {}
        except Exception as e:
            print(f"✗ Error loading data: {e}")
            return {}
    
    def create_backup(self):
        """Create timestamped backup of student data"""
        if os.path.exists(self.filename):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"student_backup_{timestamp}.json"
            try:
                with open(self.filename, 'r') as source:
                    data = json.load(source)
                with open(backup_filename, 'w') as backup:
                    json.dump(data, backup, indent=4)
                print(f"✓ Backup created: {backup_filename}")
                return True
            except Exception as e:
                print(f"✗ Backup failed: {e}")
        return False


# ==================== MODULE 3: APTITUDE TRAINING MODULE ====================
# Day 3 from Aptitude Module: Numerical Ability and Data Interpretation

class AptitudeTrainer:
    """Aptitude training and assessment module"""
    
    def __init__(self):
        self.scores = []
    
    def calculate_percentage(self, obtained: float, total: float) -> float:
        """Calculate percentage"""
        return (obtained / total) * 100 if total > 0 else 0
    
    def calculate_average(self, numbers: List[float]) -> float:
        """Calculate average of numbers"""
        return sum(numbers) / len(numbers) if numbers else 0
    
    def profit_loss(self, cost_price: float, selling_price: float) -> Dict:
        """Calculate profit or loss percentage"""
        if selling_price > cost_price:
            profit = selling_price - cost_price
            profit_percent = (profit / cost_price) * 100
            return {"type": "Profit", "amount": profit, "percent": profit_percent}
        elif cost_price > selling_price:
            loss = cost_price - selling_price
            loss_percent = (loss / cost_price) * 100
            return {"type": "Loss", "amount": loss, "percent": loss_percent}
        else:
            return {"type": "No Profit No Loss", "amount": 0, "percent": 0}
    
    def data_interpretation(self, data: List[Dict], category: str) -> Dict:
        """Interpret data from tables/charts"""
        if not data:
            return {"error": "No data provided"}
        
        values = [item.get(category, 0) for item in data if category in item]
        return {
            "total": sum(values),
            "average": sum(values) / len(values) if values else 0,
            "maximum": max(values) if values else 0,
            "minimum": min(values) if values else 0,
            "count": len(values)
        }
    
    def time_and_work(self, work_rate: float, time: float) -> float:
        """Calculate work completed given rate and time"""
        return work_rate * time
    
    def run_aptitude_quiz(self):
        """Run a sample aptitude quiz"""
        questions = [
            {"q": "What is 15% of 200?", "a": 30},
            {"q": "If a train travels 60 km in 1 hour, how far will it travel in 2.5 hours?", "a": 150},
            {"q": "Average of 10, 20, 30, 40, 50 is?", "a": 30},
        ]
        
        print("\n" + "="*50)
        print("APTITUDE QUIZ")
        print("="*50)
        
        score = 0
        for i, q in enumerate(questions, 1):
            print(f"\nQ{i}: {q['q']}")
            try:
                answer = float(input("Your answer: "))
                if answer == q['a']:
                    print("✓ Correct!")
                    score += 1
                else:
                    print(f"✗ Wrong! Answer: {q['a']}")
            except ValueError:
                print("Invalid input! Marked as incorrect.")
        
        print(f"\n{'='*50}")
        print(f"Quiz Score: {score}/{len(questions)}")
        print(f"Percentage: {(score/len(questions))*100:.1f}%")
        return score


# ==================== MODULE 4: MAIN APPLICATION ====================

class PlacementTrainingSystem:
    """Main integrated system combining all modules"""
    
    def __init__(self):
        self.student_system = StudentScoreManagementSystem()
        self.file_handler = FileHandler()
        self.aptitude_trainer = AptitudeTrainer()
        self.load_data()
    
    def load_data(self):
        """Load existing data from file"""
        data = self.file_handler.load_from_file()
        if data:
            # Convert string keys back to integers
            self.student_system.students = {int(k): v for k, v in data.items()}
    
    def save_data(self):
        """Save current data to file"""
        self.file_handler.save_to_file(self.student_system.students)
    
    def add_new_student(self):
        """Interactive student addition"""
        print("\n" + "="*50)
        print("ADD NEW STUDENT")
        print("="*50)
        
        name = input("Enter student name: ").strip()
        
        while True:
            try:
                roll_no = int(input("Enter roll number: "))
                if roll_no in self.student_system.students:
                    print("Roll number already exists!")
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
        
        # Collect skills
        print("\nEnter skills (comma-separated, e.g., Python,Java,Communication):")
        skills_input = input("Skills: ")
        skills = [s.strip().title() for s in skills_input.split(",") if s.strip()]
        
        # Collect scores for each course
        print("\nEnter scores for each subject (0-100):")
        scores = {}
        for course in ["Python", "Data Structures", "Aptitude", "Communication"]:
            while True:
                try:
                    score = int(input(f"{course}: "))
                    if 0 <= score <= 100:
                        scores[course] = score
                        break
                    else:
                        print("Score must be between 0 and 100!")
                except ValueError:
                    print("Please enter a valid number!")
        
        student = self.student_system.add_student(name, roll_no, scores, skills)
        print(f"\n✓ Student {name} added successfully!")
        self.save_data()
        return student
    
    def view_all_students(self):
        """Display all students"""
        if not self.student_system.students:
            print("\nNo students registered yet!")
            return
        
        print("\n" + "="*60)
        print("ALL STUDENTS")
        print("="*60)
        print(f"{'Roll No':<10} {'Name':<20} {'Average':<10} {'Total':<10}")
        print("-"*60)
        
        for roll, student in self.student_system.students.items():
            print(f"{roll:<10} {student['name']:<20} {student['average_score']:<10.1f} {student['total_score']:<10}")
    
    def generate_report(self):
        """Generate training report"""
        if not self.student_system.students:
            print("\nNo data available for report generation!")
            return
        
        print("\n" + "="*60)
        print("TRAINING REPORT - RUBICON INDUSTRY-ORIENTED PROGRAM")
        print("="*60)
        print(f"Report Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Students Enrolled: {len(self.student_system.students)}")
        
        # Statistics
        all_avg_scores = [s['average_score'] for s in self.student_system.students.values()]
        class_avg = sum(all_avg_scores) / len(all_avg_scores) if all_avg_scores else 0
        
        print(f"\nClass Statistics:")
        print(f"  - Class Average Score: {class_avg:.2f}")
        print(f"  - Highest Score: {max(all_avg_scores):.2f}")
        print(f"  - Lowest Score: {min(all_avg_scores):.2f}")
        
        # Top performers
        print(f"\nTop 3 Performers:")
        top_students = self.student_system.get_top_performers(3)
        for i, student in enumerate(top_students, 1):
            print(f"  {i}. {student['name']} (Roll: {student['roll_no']}) - {student['average_score']:.2f}%")
        
        print("="*60)
    
    def run(self):
        """Main menu system"""
        while True:
            print("\n" + "="*50)
            print("RUBICON PLACEMENT TRAINING SYSTEM")
            print("="*50)
            print("1. Add New Student")
            print("2. View Student Details")
            print("3. Update Student Score")
            print("4. View All Students")
            print("5. Run Aptitude Quiz")
            print("6. Generate Training Report")
            print("7. Create Backup")
            print("8. Exit")
            print("-"*50)
            
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == "1":
                self.add_new_student()
            
            elif choice == "2":
                try:
                    roll = int(input("Enter roll number: "))
                    self.student_system.display_student_summary(roll)
                except ValueError:
                    print("Invalid roll number!")
            
            elif choice == "3":
                try:
                    roll = int(input("Enter roll number: "))
                    subject = input("Enter subject name: ")
                    score = int(input("Enter new score: "))
                    if self.student_system.update_score(roll, subject, score):
                        print("✓ Score updated successfully!")
                        self.save_data()
                    else:
                        print("Failed to update score!")
                except ValueError:
                    print("Invalid input!")
            
            elif choice == "4":
                self.view_all_students()
            
            elif choice == "5":
                self.aptitude_trainer.run_aptitude_quiz()
            
            elif choice == "6":
                self.generate_report()
            
            elif choice == "7":
                self.file_handler.create_backup()
            
            elif choice == "8":
                print("\nSaving data before exit...")
                self.save_data()
                print("Thank you for using Rubicon Placement Training System!")
                print("Good luck with your placements!")
                break
            
            else:
                print("Invalid choice! Please select 1-8.")


# ==================== PROGRAM ENTRY POINT ====================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("RUBICON INDUSTRY-ORIENTED SKILL DEVELOPMENT PROGRAM")
    print("Department of Computer Engineering")
    print("Zeal College of Engineering & Research, Pune")
    print("="*60)
    print("\nWelcome to the Placement Training System!")
    
    system = PlacementTrainingSystem()
    system.run()
